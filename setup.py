from setuptools import setup, find_packages

setup(
    name='tradutor-de-binario',
    version='1.0.0',
    description='Um tradutor de binário para ascii (texto) fácil de usar',
    url='https://github.com/bernardofreitas/tradutor-de-binario',
    author='Bernardo Freitas',
    author_email='bernard0freitas@outlook.com',
    packages=find_packages(),
    scripts=['tradutor.py'],
    install_requirements=['click']
    )

