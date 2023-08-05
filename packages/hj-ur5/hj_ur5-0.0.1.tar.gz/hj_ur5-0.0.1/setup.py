import setuptools
from pathlib import Path


setuptools.setup(
    name='hj_ur5',
    version='0.0.1',
    description='IAS Lab ur5',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(include='ur_gym*'),
    install_requires=['gym']
)