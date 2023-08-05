from os import path

from setuptools import find_packages, setup

dirname = path.abspath(path.dirname(__file__))
with open(path.join(dirname, 'README.md')) as f:
    long_description = f.read()

setup(
    name='featuretoolsOnSparkX',
    version='0.3.0',
    packages=find_packages(),
    description='a bugfix version for raw repo',
    license='MIT',
    url='https://github.com/tzbo/featuretoolsOnSpark',
    author='giantcroc',
    author_email='ringer0910@gmail.com',
    classifiers=[
         'Development Status :: 2 - Pre-Alpha',
         'Intended Audience :: Developers',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.5',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7'
    ],
    install_requires=open('requirements.txt').readlines(),
    python_requires='>=2.7, <4',
    keywords='feature engineering data science machine learning',
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
