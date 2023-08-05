from setuptools import find_packages, setup
from llmbda_fastapi import __version__

core_reqs = [
    "fastapi~=0.95.0",
    "pydantic~=1.10.7",
    "requests~=2.28.2",
    "six~=1.16.0",
    "sniffio~=1.3.0",
    "starlette~=0.26.1",
    "tqdm~=4.65.0",
    "typing_extensions~=4.5.0",
    "tzdata~=2023.3",
    "urllib3~=1.26.15",
    "uvicorn~=0.21.1",
    "wincertstore~=0.2",
]

setup(
    name="llmbda_fastapi",
    version=__version__,
    url="https://relevanceai.com/",
    author="Relevance AI",
    author_email="jacky@relevanceai.com",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    setup_requires=["wheel"],
    install_requires=core_reqs,
    package_data={"": ["*.ini"]},
    extras_require=dict(),
)
