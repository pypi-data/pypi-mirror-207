from setuptools import find_packages, setup

setup(
    name="toolforge-weld",
    version="0.1.0.1",
    author="Taavi Väänänen",
    author_email="hi@taavi.wtf",
    license="AGPL-3.0-or-later",
    packages=find_packages(),
    package_data={"toolforge_weld": ["py.typed"]},
    description="Shared Python code for Toolforge infrastructure components",
    install_requires=["python-dateutil", "PyYAML", "requests"],
    python_requires=">=3.7",
)
