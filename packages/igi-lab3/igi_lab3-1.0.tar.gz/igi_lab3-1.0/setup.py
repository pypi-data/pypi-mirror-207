from setuptools import setup


setup(
    name="igi_lab3",
    version="1.0",
    description="library for python serialization",
    url="https://github.com/Tivlas/IGI-Labs-2023/tree/lab3/lab3",
    author="Timofey Vlasenko",
    author_email="tima051003@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["serializers/json_serializer", "serializers/src",
              "serializers/xml_serializer", "serializers"],
    include_package_data=True
)
