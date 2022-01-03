import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enumerate-markdown",
    version="1.0.0",
    author="Assaf Yifrach",
    author_email="asafyi@gmail.com",
    description="Enumerates your markdown headers, inside the md file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a4vision/enumerate-markdown",
    packages=[p for p in setuptools.find_packages() if p != 'tests'],
    install_requires=[
        "mistune>=2.0",
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    scripts=['bin/markdown-enum'],
)
