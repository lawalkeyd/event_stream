from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in event_stream/__init__.py
from event_stream import __version__ as version

setup(
	name="event_stream",
	version=version,
	description="Simplified Event Streaming",
	author="Kayode Lawal",
	author_email="lawalkeyd@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
