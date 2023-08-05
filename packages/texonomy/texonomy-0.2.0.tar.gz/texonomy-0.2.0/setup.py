from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name="texonomy", include_package_data=True, package_data={'': ['templates/template.tex']}, packages=find_packages(), version="0.2.0", long_description=readme, long_description_content_type='text/markdown'
)
