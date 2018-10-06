import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recommerce-crawler",
    version="0.1",
    author="Archit Dwivedi",
    author_email="architdwivedi@@gmail.com",
    description="A sample package to crawl ecommerce websites for reviews",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/archit0/ecommerce-crawler",
    packages=setuptools.find_packages(),
    classifiers=[
    ],
)