from setuptools import setup

setup(
    name="scoi_lab_serializer_package",
    version="0.1",
    description="package for python (de)serialization in .json and .xml",
    url="https://github.com/DrVaroZ/SCoL_labs/tree/lab3",
    author="Vadim Zhur",
    author_email="vadim10zhur@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["serializers/json", "serializers/source", "serializers/xml", "serializers"],
    include_package_data=True
)
