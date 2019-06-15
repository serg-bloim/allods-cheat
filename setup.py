from setuptools import setup, find_packages
from version import __version__

setup(name='aoe2stats',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'psutil >= 5.6.2',
        'Flask==1.0.2',
        'Flask-RESTful==0.3.7'
    ],
)

