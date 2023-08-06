from setuptools import setup, find_packages

setup(
    name='pyfoundt',
    packages=find_packages(),
    version='0.8.1',
    install_requires=[
        "requests"
    ],
    author="ZuoYihan(左易晗)[china(中国)]",
    description="一个普通的模块\nA regular module",
    long_description="一个简洁且易于上手的一种包含了Python语言一些常用操作的模块\nA concise and user-friendly module that includes some "
                     "commonly used operations in the Python language.",
    platforms=["Windows", "Linux"],
    python_requires='>=3',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ]
)
