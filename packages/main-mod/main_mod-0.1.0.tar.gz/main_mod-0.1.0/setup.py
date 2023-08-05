from setuptools import setup, find_packages

setup(
    name='main_mod',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your module dependencies here
    ],
    entry_points={
        'console_scripts': [
            'main_mod = main_mod.main_module:main',
        ],
    },
)

from setuptools import setup, find_packages

setup(
    name="main_mod",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    author="putkoff",
    author_email="putkey2@sbcglobal.net",
    description="putkoffs stuff",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/main_mod",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
from setuptools import setup, find_packages

setup(
    name="putkoff_mod",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    author="putkoff",
    author_email="putkey2@sbcglobal.net",
    description="putkoffs stuff",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/putkoff_mod",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
