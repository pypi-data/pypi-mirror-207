import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EasyForge",
    version="0.0.2",
    author="DKVG",
    author_email="gadellidk@gmail.com",
    description="To Make easy to use Forge (APS) by python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    keywords='EasyForge forge APS forge-python python-aps',
)
