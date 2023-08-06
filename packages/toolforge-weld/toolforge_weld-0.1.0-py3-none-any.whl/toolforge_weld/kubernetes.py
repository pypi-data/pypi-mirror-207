import os
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, ClassVar, Dict, List, Optional, Union

import requests
import urllib3
import yaml

import toolforge_weld
from toolforge_weld.errors import ToolforgeError


class ToolforgeKubernetesError(ToolforgeError):
    """Base class for exceptions related to the Kubernetes client."""


class KubernetesConfigFileNotFoundException(ToolforgeKubernetesError):
    """Raised when a Kubernetes client is attempted to be created but the configuration file does not exist."""


def _find_cfg_obj(config, kind, name):
    """Lookup a named object in a config."""
    for obj in config[kind]:
        if obj["name"] == name:
            return obj[kind[:-1]]
    raise ToolforgeKubernetesError(
        "Key {} not found in {} section of config".format(name, kind)
    )


def _resolve_file_path(base: Path, input: str) -> Path:
    input_path = Path(input).expanduser()
    if input_path.is_absolute():
        return input_path
    return (base / input_path).resolve()


class K8sClient:
    """Kubernetes API client."""

    VERSIONS: ClassVar[Dict[str, str]] = {
        "configmaps": "v1",
        "cronjobs": "batch/v1",
        "deployments": "apps/v1",
        "endpoints": "v1",
        "events": "v1",
        "ingresses": "networking.k8s.io/v1",
        "jobs": "batch/v1",
        "limitranges": "v1",
        "pods": "v1",
        "replicasets": "apps/v1",
        "resourcequotas": "v1",
        "services": "v1",
    }

    def __init__(
        self,
        *,
        server: str,
        namespace: str,
        tls_cert_file: Path,
        tls_key_file: Path,
        tls_verify_ca: Union[Path, bool],
        user_agent: str,
        timeout: int = 10,
    ):
        """Constructor."""
        self.timeout = timeout
        self.server = server
        self.namespace = namespace
        self.session = requests.Session()

        self.session.cert = (str(tls_cert_file), str(tls_key_file))

        if isinstance(tls_verify_ca, Path):
            self.session.verify = str(tls_verify_ca.resolve())
        else:
            self.session.verify = tls_verify_ca

            # T253412: Disable warnings about unverifed TLS certs when talking to the
            # Kubernetes API endpoint
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.session.headers[
            "User-Agent"
        ] = f"{user_agent} toolforge_weld/{toolforge_weld.__version__} python-requests/{requests.__version__}"

    @classmethod
    def from_file(cls, file: Path, **kwargs) -> "K8sClient":
        """Create a client from a kubeconfig file."""
        if not file.exists():
            raise KubernetesConfigFileNotFoundException(str(file.resolve()))

        data = yaml.safe_load(file.read_text())
        context = _find_cfg_obj(data, "contexts", data["current-context"])
        cluster = _find_cfg_obj(data, "clusters", context["cluster"])
        user = _find_cfg_obj(data, "users", context["user"])

        return cls(
            server=cluster["server"],
            namespace=context["namespace"],
            tls_cert_file=_resolve_file_path(file.parent, user["client-certificate"]),
            tls_key_file=_resolve_file_path(file.parent, user["client-key"]),
            tls_verify_ca=False,
            **kwargs,
        )

    @staticmethod
    def locate_config_file() -> Path:
        """Attempt to locate the Kubernetes config file for this user."""
        return Path(os.getenv("KUBECONFIG", "~/.kube/config")).expanduser()

    def _make_kwargs(self, url: str, **kwargs):
        """Setup kwargs for a Requests request."""
        version = kwargs.pop("version", "v1")
        if version == "v1":
            root = "api"
        else:
            root = "apis"

        # use "or" syntax in case namespace is present but set as None
        namespace = kwargs.pop("namespace", None) or self.namespace

        kwargs["url"] = "{}/{}/{}/namespaces/{}/{}".format(
            self.server, root, version, namespace, url
        )

        name = kwargs.pop("name", None)
        if name is not None:
            kwargs["url"] = "{}/{}".format(kwargs["url"], name)

        subpath = kwargs.pop("subpath", None)
        if subpath is not None:
            kwargs["url"] = "{}{}".format(kwargs["url"], subpath)

        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout

        return kwargs

    def _get(self, url, **kwargs):
        """GET request."""
        r = self.session.get(**self._make_kwargs(url, **kwargs))
        r.raise_for_status()
        return r.json()

    def _post(self, url, **kwargs):
        """POST request."""
        r = self.session.post(**self._make_kwargs(url, **kwargs))
        r.raise_for_status()
        return r.status_code

    def _put(self, url, **kwargs):
        """PUT request."""
        r = self.session.put(**self._make_kwargs(url, **kwargs))
        r.raise_for_status()
        return r.status_code

    def _delete(self, url, **kwargs):
        """DELETE request."""
        r = self.session.delete(**self._make_kwargs(url, **kwargs))
        r.raise_for_status()
        return r.status_code

    def get_object(
        self,
        kind: str,
        name: str,
        *,
        namespace: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get the object with the specified name and of the given kind in the namespace."""
        return self._get(
            kind,
            name=name,
            version=K8sClient.VERSIONS[kind],
            namespace=namespace,
        )

    def get_objects(
        self,
        kind: str,
        *,
        label_selector: Optional[Dict[str, str]] = None,
        field_selector: Optional[Dict[str, Any]] = None,
        namespace: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Get list of objects of the given kind in the namespace."""
        params: Dict[str, Any] = {}

        if label_selector:
            params["labelSelector"] = ",".join(
                [f"{k}={v}" for k, v in label_selector.items()]
            )
        if field_selector:
            params["fieldSelector"] = field_selector

        return self._get(
            kind,
            params=params,
            version=K8sClient.VERSIONS[kind],
            namespace=namespace,
        )["items"]

    def delete_objects(
        self,
        kind: str,
        *,
        label_selector: Optional[Dict[str, str]] = None,
    ):
        """Delete objects of the given kind in the namespace."""
        if kind == "services":
            # Annoyingly Service does not have a Delete Collection option
            for svc in self.get_objects(kind, label_selector=label_selector):
                self._delete(
                    kind,
                    name=svc["metadata"]["name"],
                    version=K8sClient.VERSIONS[kind],
                )
        else:
            self._delete(
                kind,
                params={"labelSelector": label_selector},
                version=K8sClient.VERSIONS[kind],
            )

    def create_object(self, kind: str, spec: Dict[str, Any]):
        """Create an object of the given kind in the namespace."""
        return self._post(
            kind,
            json=spec,
            version=K8sClient.VERSIONS[kind],
        )

    def replace_object(self, kind: str, spec: Dict[str, Any]):
        """Replace an object of the given kind in the namespace."""
        return self._put(
            kind,
            json=spec,
            name=spec["metadata"]["name"],
            version=K8sClient.VERSIONS[kind],
        )


# Copyright 2019 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
def parse_quantity(quantity):
    """
    Parse kubernetes canonical form quantity like 200Mi to a decimal number.
    Supported SI suffixes:
    base1024: Ki | Mi | Gi | Ti | Pi | Ei
    base1000: n | u | m | "" | k | M | G | T | P | E
    See https://github.com/kubernetes/apimachinery/blob/master/pkg/api/resource/quantity.go # noqa
    Input:
    quanity: string. kubernetes canonical form quantity
    Returns:
    Decimal
    Raises:
    ValueError on invalid or unknown input
    """

    if isinstance(quantity, (int, float, Decimal)):
        return Decimal(quantity)

    exponents = {
        "n": -3,
        "u": -2,
        "m": -1,
        "K": 1,
        "k": 1,
        "M": 2,
        "G": 3,
        "T": 4,
        "P": 5,
        "E": 6,
    }
    quantity = str(quantity)
    number = quantity
    suffix = None

    if len(quantity) >= 2 and quantity[-1] == "i":
        if quantity[-2] in exponents:
            number = quantity[:-2]
            suffix = quantity[-2:]
    elif len(quantity) >= 1 and quantity[-1] in exponents:
        number = quantity[:-1]
        suffix = quantity[-1:]

    try:
        number = Decimal(number)
    except InvalidOperation:
        raise ValueError("Invalid number format: {}".format(number))

    if suffix is None:
        return number
    if suffix.endswith("i"):
        base = 1024
    elif len(suffix) == 1:
        base = 1000
    else:
        raise ValueError("{} has unknown suffix".format(quantity))

    # handly SI inconsistency
    if suffix == "ki":
        raise ValueError("{} has unknown suffix".format(quantity))
    if suffix[0] not in exponents:
        raise ValueError("{} has unknown suffix".format(quantity))

    exponent = Decimal(exponents[suffix[0]])
    return number * (base**exponent)
