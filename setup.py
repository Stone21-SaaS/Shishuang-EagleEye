from setuptools import setup, find_packages

setup(
    name="Shishuang-EagleEye",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "python-nmap",
        "scapy",
    ],
    entry_points={
        "console_scripts": [
            "eagle-eye=src.main:main",
        ],
    },
)
