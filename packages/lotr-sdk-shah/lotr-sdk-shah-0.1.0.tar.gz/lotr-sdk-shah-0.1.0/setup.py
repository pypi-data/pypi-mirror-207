from setuptools import setup, find_packages

setup(
    name="lotr-sdk-shah",
    version="0.1.0",
    description="A Python SDK for The Lord of the Rings API",
    author="loveshah",
    author_email="lks9@njit.edu",
    url="https://github.com/Shahupdates/love-shah-SDK",
    packages=find_packages(),
    install_requires=[
        "requests",
        "requests_cache",
        "ratelimiter",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
