import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pokerpy-c1au6io-dottorDav", # Replace with your own username
    version="0.0.0.9",
    author="Claudio Zanettini, Davide Colella",
    author_email="claudio.zanettini@gmail.com, dottordav@gmail.com  ",
    description="An implementation of the classical poker in Python",
    long_description="""
    The aim of this project is to develop in `python` the classical power game, and in the process to learn more about `python`,
    probability and game theory and deep inside about our-selves and the meaning of life.

    We are well aware that there are many other people that did it already in python (es: [link](https://pypi.org/project/poker/)) 
    and that poker is quite complex, but again this is an exercise for us, and being able to take a peak at the work of someone 
    else (much more experience then us) makes it even more informative.
    """
    ,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'pandas',
        'numpy'
    ],
    python_requires='>=3.6',
)