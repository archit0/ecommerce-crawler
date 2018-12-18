import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ecommerce-crawler",
    version="0.1",
    author="Archit Dwivedi",
    author_email="architdwivedi@@gmail.com",
    description="Package to crawl ecommerce websites for reviews",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/archit0/ecommerce-crawler",
    packages=setuptools.find_packages(),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: Non-Free',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    install_requires=['bs4==0.0.1', 'requests==2.21.0', ],
)
