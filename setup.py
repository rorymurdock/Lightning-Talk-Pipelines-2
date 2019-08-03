import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lightning-talk-pipelines",
    version="0.0.4",
    author="Rory Murdock",
    author_email="rory@itmatic.com.au",
    description="A sample package for testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rorymurdock/Lightning-Talk-Pipelines-2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)