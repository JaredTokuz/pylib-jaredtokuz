import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="widely-used-functions",
    version="0.0.3",
    author="Jared Tokuz",
    author_email="jtokuz@gmail.com",
    description="Installation of Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JaredTokuz/WidelyUsedFunctions",
    project_urls={
        "Bug Tracker": "https://github.com/JaredTokuz/WidelyUsedFunctions/issues"
    },
    license="MIT",
    packages=["widely-used-functions"],
    install_requires=[],
)
