import setuptools

setuptools.setup(
    name="test1library",
    version="1.0.0",
    author="devanshi",
    author_email="awasthidevanshi1155@gmail.com",
    description="description",
    long_description="long description",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "your-dependency1",
        "your-dependency2",
        # add any other dependencies here
    ],
    test_suite="tests",
    tests_require=[
        "pytest",
        # add any other testing dependencies here
    ],
)
