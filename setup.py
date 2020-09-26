import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

project_urls = {
    "Homepage": "https://github.com/eocode/ISO8583-Dlib",
    "Issue tracker": "https://github.com/eocode/ISO8583-Dlib/issues",
    "Code": "https://github.com/eocode/ISO8583-Dlib",
    "Documentation": "https://github.com/eocode/ISO8583-Dlib/wiki",
}

setuptools.setup(
    name='ISO8583-Dlib',
    version='0.1.3',
    author='eocode',
    author_email='hola@eliasojedamedina.com',
    license='MIT license',
    description='Parser String to JSON for ISO8583 Package',
    long_description_content_type="text/markdown",
    long_description=open("README.md").read()
    + "\n\n"
    + open("CHANGELOG.md").read(),
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    project_urls=project_urls,
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.6",
)
