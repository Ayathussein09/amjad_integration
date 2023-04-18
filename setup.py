from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in amjad_integration/__init__.py
from amjad_integration import __version__ as version

setup(
	name="amjad_integration",
	version=version,
	description="amjad_integration",
	author="Madkour",
	author_email="ayat.hussein@madkour.com.eg",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
