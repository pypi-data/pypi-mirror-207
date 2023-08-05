from setuptools import setup, find_packages

setup(
    name='skidrow_logger',
    version='0.1.0',
    author='amitskidrow',
    author_email='amitskidrow@gmail.com',
    description='My Python package',
    packages=find_packages(),
    install_requires=[
        'snakecase',
    ]
)
