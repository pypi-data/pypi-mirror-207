import setuptools 

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="ProcessingImg1",
    version="0.2",
    author="Alaa Jassim Mohammed",
    author_email = "alobede2001alobede@gmail.com",
    url="https://github.com/Alaa-Jassim/proc-image",
    description="A simple Pythonic library for image manipulation and hardware configuration that you can use alongside your project to save you time and effort",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ]
    )
