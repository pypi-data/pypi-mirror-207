import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='simple-glogging',
    version='1.0',
    author='Rishiraj verma',
    author_email='rishiraj.verma@galaxyweblinks.co.in',
    description='A library to use logging Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/GWL-rishiraj/simplelogging',
    project_urls = {
        "Bug Tracker": "https://github.com/GWL-rishiraj/simplelogging/issues"
    },
    license='MIT',
    packages=['simple-glogging'],
    install_requires=['PyYAML'],
)
