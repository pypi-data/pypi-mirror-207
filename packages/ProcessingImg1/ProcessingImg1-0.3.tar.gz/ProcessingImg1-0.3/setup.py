
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ProcessingImg1",
    version="0.3",
    author="علاء جاسم محمد",
    author_email="alobede2001alobede@gmail.com",
    description="A simple Pythonic library for image manipulation and hardware configuration that you can use alongside your project to save you time and effort",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alaa-Jassim/proc-image",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)