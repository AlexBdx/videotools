import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="videotools",
    version="0.0.18",
    author="Alex Bondoux",
    author_email="alexandre.bdx@gmail.com",
    description="A collection of helper functions to process videos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexBdx/Heli/tree/master/videotools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
)
