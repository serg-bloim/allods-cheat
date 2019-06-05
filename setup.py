from setuptools import setup, find_packages

setup(
    name='aoe2stats',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'psutil >= 5.6.2',
        'Flask==1.0.2',
        'Flask-RESTful==0.3.7'
    ],
)
