from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pysangkom',
    version='1.0.4',
    packages=find_packages(),
    author='m_keen',
    author_email='vxfqkn8wtx@privaterelay.appleid.com',
    description='This library is pysangkom, Please becareful',
    long_description=long_description,
    long_description_content_type='text/markdown',
    readme = "README.md",
    install_requires=[
        'numpy>=1.24.0',
        'requests>=2.30.0'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
