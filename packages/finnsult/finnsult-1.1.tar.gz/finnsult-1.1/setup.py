import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "finnsult",
    version = "1.01",
    author = "Finn Everspaugh",
    author_email = "finnventor@everspaugh.com",
    description = "A program to insult people",
    entry_points={
        'console_scripts': [
            'insult = insult:main',
       ],
    },
    include_package_data=True,
    install_requires=['pyyaml'],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://the-real-finnventor.github.io/insult/",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    package_dir = {"": "src"},
    packages = ['insult'],
)