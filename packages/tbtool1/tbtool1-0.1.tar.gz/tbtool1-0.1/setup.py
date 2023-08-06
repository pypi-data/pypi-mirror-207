from setuptools import find_packages
import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt","r") as req:
    required_packages = req.read().splitlines()

setuptools.setup(
    name="tbtool1",                
    version="0.1",                        
    author="Bhanuja",  
    author_email="abhanuja@presidio.com",
    license= 'MIT',              
    description="Data And Analytics Audit Tool",
    long_description=long_description,     
    long_description_content_type="text/markdown",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        'common': ['templates/*.html']
    },
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'tbtool1=main:Main.generate_aws_audit_report'
        ]
    },
    include_package_data=True,
    python_requires='>=3.6',                
    install_requires=required_packages                   
)