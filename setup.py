from setuptools import setup, find_packages


def get_description():
    return "Deep Learning library for colorizing and restoring old images and video"


def get_long_description():
    with open("README.md") as f:
        return f.read()


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="DeOldify",
    version="1.0.0",
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/jantic/DeOldify",
    license="MIT License",
    description=get_description(),
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=get_requirements(),
)
