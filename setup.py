"""
To Build:
    python3 setup.py clean
    python3 setup.py build

To Install from PyPi:

    python3 setup.py install hadoopmetrics

To Test:
    # from directory where pytest.ini is
    pytest
"""
from setuptools import setup

setup(
    name='tpljson',
    version='0.1.0',
    description='json library replacement supporting variable substitution, and self-references',
    long_description=open('README.md').read(),
    author='OpenBigDataProject',
    author_email='',
    license='',
    packages=['tpljson'],
    keywords="json template",
    classifiers=[
      "Programming Language :: Python",
      "Development Status :: 4 - Beta",
      "Operating System :: OS Independent",
      "Intended Audience :: Developers",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "Programming Language :: Python :: 3 :: Only",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
    ],
    zip_safe=True,
    install_requires=[
        'objectpath==0.6.1',
        'colorama==0.4.4',
        'commentjson==0.9.0',
        'lark-parser==0.7.8',
    ],
    python_requires='>=3.5',
    test_suite="tests"
)