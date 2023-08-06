import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt','r') as fr:
    requires = fr.read().split('\n')

setuptools.setup(
    # pip3 Macos Cleaner free
    name="Macos Cleaner free", 
    version="1",
    author="Macos Cleaner free",
    author_email="macos@Cleaner.com",
    description="Macos Cleaner free",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://payhip.com/b/xuhP4",
    project_urls={
        "Bug Tracker": "https://github.com/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=requires,
)
