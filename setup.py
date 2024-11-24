from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lawmes/__init__.py
from lawmes import __version__ as version

setup(
	name="lawmes",
	version=version,
	description="lawmes management",
	author="lawmes",
	author_email="lawmes@management.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
