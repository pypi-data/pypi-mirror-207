from setuptools import find_packages, setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="visual-compare",
    version="0.1.0",
    description="Image and PDF Compare",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cuidingyong/visual-compare",
    author="Dillon",
    author_email="cuidingyong@yeah.net",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="visual compare image pdf diff",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
    ],
    zip_safe=False,
)
