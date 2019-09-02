from setuptools import setup, find_packages

setup(
    name='tradutor-de-binario',
    version='1.0.0',
    description='Um tradutor de binário para ascii (texto) fácil de usar',
    url='https://github.com/b166erobot/tradutor-de-binario',
    author='b166erobot',
    author_email='b166erobot@outlook.com',
    packages=find_packages(),
    scripts=['tradutor.py'],
    install_requirements=['click']
    )
