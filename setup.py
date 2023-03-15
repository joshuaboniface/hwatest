from setuptools import setup

setup(
    name="hwatest",
    version="0.1",
    packages=["hwatest"],
    install_requires=[
        "Click",
        "distro",
    ],
    entry_points={
        "console_scripts": [
            "hwatest = hwatest.hwatest:cli",
        ],
    },
)
