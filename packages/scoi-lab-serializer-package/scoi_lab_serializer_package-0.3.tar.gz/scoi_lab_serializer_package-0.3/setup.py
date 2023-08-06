from setuptools import setup

setup(
    name="scoi_lab_serializer_package",
    version="0.3",
    description="package for python (de)serialization in .json and .xml",
    url="https://github.com/DrVaroZ/SCoL_labs/tree/lab3",
    author="Vadim Zhur",
    author_email="vadim10zhur@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["scoi_lab_serializer_package/json", "scoi_lab_serializer_package/source", "scoi_lab_serializer_package/xml", "scoi_lab_serializer_package"],
    include_package_data=True
)
