from setuptools import setup, find_packages


setup(
    name="my_serializer",
    version="1.42",
    description="Library for serialization/deserialization of objects in python(json, xml)",
    url="https://github.com/SergeyBrykulskii/IGI_Labs/tree/Lab3/Lab3",
    author="Sergey Brykulskii",
    author_email="serxio6758@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["parsers/json", "parsers/src", "parsers/xml"],
    include_package_data=True
)