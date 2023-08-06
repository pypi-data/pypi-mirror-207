from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="sublinear",
    version="0.1.0",
    description="Python library implementing a subset of streaming algorithms. Includes variations of these algorithms (e.g. adversarially robust), as well as support for multiple data types.",
    long_description_content_type='text/markdown',
    long_description=long_description,
    license="MIT",
    author="Ivan Nikitovic",
    author_email="ivan.bnikitovic@gmail.com",
    url="https://github.com/ivannikitovic/sublinear",
    packages=find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=[
        'numpy',
        'matplotlib',
    ],
)