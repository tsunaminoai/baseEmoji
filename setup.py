from setuptools import setup, find_packages

setup(
    name="baseEmoji",
    version = '0.1.1',
    description="A simple base1024 encoder that outputs emoji.",
    long_description='baseEmoji is a base1024 encoding scheme that uses emoji as its lookup table. The primary purpose is to represent otherwise ugly data in more "pleasing" form in social media.',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6"
    ],
    keywords="base1024 encode emoji",
    author="Ben Craton",
    author_email="tsunaminoai@gmail.com",
    url="http://github.com/tsunaminoai/baseemoji",
    license="MIT",
    packages=find_packages(exclude=["test",]),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        "uniseg",
    ],
    tests_require=[],
    test_suite="test"
)
