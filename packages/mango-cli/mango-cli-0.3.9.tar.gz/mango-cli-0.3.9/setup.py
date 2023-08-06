from setuptools import setup, find_packages
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='mango-cli',
    version="0.3.9",
    packages=find_packages(),
    author='Mangosoft',
    author_email="wilson.mendoza@mango-soft.com",
    description="Mangosoft CLI",
    py_modules=["app"],
    include_dirs=["app"],
    includes=["VERSION"],
    install_requires=[requirements],
    entry_points='''
        [console_scripts]
        mango=app.application:cli
    '''
)
    