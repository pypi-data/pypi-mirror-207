import setuptools
long_desc = open("README.md").read()
setuptools.setup(
    name="asciicards",
    version="0.0.3", # eg:1.0.0
    author="PaperJam",
    author_email="archood2@gmail.com",
    license="GNU General Public License v3.0",
    description="Ascii Card Library",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/ArchooD2/asciicards",
    packages = [],
    # project_urls is optional
    python_requires=">=3.6",
)
