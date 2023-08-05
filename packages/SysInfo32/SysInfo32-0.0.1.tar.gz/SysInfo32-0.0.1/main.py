
import os
import shutil

from setuptools import setup


description = 'SysInfo32'

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Programming Language :: Python :: 3'
]

keywords = [
    'python'
]

packages = ['']


setup(
    name='SysInfo32',
    version='0.0.1',
    description='upcoming project',
    long_description='upcoming project, releasing soon',
    url='https://github.com/Bamboooz/SysInfo32',
    author='Bamboooz',
    author_email='bambusixmc@gmail.com',
    license='BSD-3-Clause',
    classifiers=classifiers,
    keywords=keywords,
    packages=packages
)


if __name__ == '__main__':
    # run this file using python setup.py sdist bdist_wheel
    password = input('Enter your pypi password: ')
    os.system(f'twine upload --repository-url https://upload.pypi.org/legacy/ -u Bamboooz -p {password} dist/*')

    # remove pypi build directories
    shutil.rmtree(f'{os.getcwd()}\\build')
    shutil.rmtree(f'{os.getcwd()}\\dist')
    shutil.rmtree(f"{os.getcwd()}\\{[d for d in os.listdir('.') if os.path.isdir(d) and 'egg-info' in d][0]}")