from setuptools import setup, find_packages

setup(
    name='youcan',
    version='1.0.0',
    author='Adam Louly',
    author_email='adamlouly3@gmail.com',
    description='YOUcan Python SDK',
    packages=find_packages(),
    install_requires=[
        'requests',
        # Add any other dependencies your SDK requires
    ],
)
