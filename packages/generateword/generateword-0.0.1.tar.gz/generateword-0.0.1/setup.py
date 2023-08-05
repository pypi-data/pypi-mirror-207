import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="generateword",
    version="0.0.1",
    author="Your Name",
    description="A library for generating random words",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/generateword",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)