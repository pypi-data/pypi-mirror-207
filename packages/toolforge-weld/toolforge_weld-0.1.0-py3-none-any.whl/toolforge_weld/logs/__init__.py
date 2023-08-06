"""Queries logs created by a tool."""
from toolforge_weld.kubernetes import K8sClient
from toolforge_weld.logs.kubernetes import KubernetesSource
from toolforge_weld.logs.source import LogEntry, LogSource


def get_log_source(user_agent: str) -> LogSource:
    """Gets a suitable log source implementation."""
    k8s_client = K8sClient.from_file(
        file=K8sClient.locate_config_file(), user_agent=f"{user_agent} logs"
    )

    return KubernetesSource(client=k8s_client)


__all__ = ["LogSource", "LogEntry", "get_log_source"]
