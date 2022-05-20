from setuptools import setup

setup(
    name="memray",
    version="1.1.0",
    author="VyOS maintainers and contributors",
    author_email="maintainers@vyos.net",
    python_requires=">=3.9",
    license="BSD",
    url="http://www.vyos.io",
    packages=["memray"],
    description=("A debian wrapper of memray."),
)
