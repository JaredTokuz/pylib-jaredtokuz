import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylibjaredtokuz",
    version="0.0.41",
    author="Jared Tokuz",
    author_email="jtokuz@gmail.com",
    description="Installation of Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JaredTokuz/pylib-jaredtokuz",
    project_urls={
        "Bug Tracker": "https://github.com/JaredTokuz/pylib-jaredtokuz/issues"
    },
    license="MIT",
    packages=["pylibjaredtokuz"],
    install_requires=["python-dotenv"],
)
