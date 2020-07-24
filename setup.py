import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="mullvad_api",
    version="1.0.0",
    author="meichthys",
    description="Python wrapper around mullvad api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests"],
    py_modules=["mullvad_api"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Networking",
    ],
)
