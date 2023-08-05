import re
import pathlib

import setuptools
from setuptools import setup

name = "usda_api"
here = pathlib.Path.absolute(pathlib.Path(__file__).resolve().parent)

# get package version
with open(pathlib.Path(here, f"src/{name}/__init__.py"), encoding="utf-8") as f:
    result = re.search(r'__version__ = ["\']([^"\']+)', f.read())

    if not result:
        raise ValueError(
            f"Can't find the version in {pathlib.Path(here, f'src/{name}/__init__.py')}"
        )

    version = result.group(1)


def get_long_description():
    with open("./README.md", "r", encoding="utf-8") as fh:
        return fh.read()


base_requirements = {
    "typing_extensions>=3.7.4.3 ;  python_version < '3.8'",
    "typing_extensions>=3.10.0.2 ;  python_version >= '3.8'",
    "mypy_extensions>=0.4.3",
    "typing-inspect",
    "pydantic>=1.5.1",
    "mixpanel>=4.9.0",
}

framework_common = {
    "pandas==2.0.0",
}

dev_requirements = {
    "black==22.10.0",
    "pip-chill==1.0.1",
    "pre-commit==2.20.0",
    "coverage>=5.1",
    "flake8>=3.8.3",
    "flake8-tidy-imports>=4.3.0",
    "isort>=5.7.0",
    "mypy==0.991",
    "pytest>=6.2.2",
    "pytest-testmon==1.4.2",
    "pytest-asyncio==0.20.3",
    "vulture==2.7",
}

setup(
    name=name,
    version=version,
    author="Loh YI Kuang",
    description=get_long_description(),
    long_description=get_long_description(),
    license="Apache License 2.0",
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="./src"),
    package_data={name: ["*.txt", "*.json", "*.preamble", "*.sql"]},
    entry_points={"console_scripts": [f"{name}={name}.entrypoints:main"]},
    python_requires=">=3.9",
    install_requires=list(base_requirements | framework_common),
    extras_require={"dev": list(dev_requirements)},
)
