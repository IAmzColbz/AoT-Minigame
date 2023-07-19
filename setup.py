from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='AoTMinigame',
    version='0.1.0',
    description='Learning Project based on Attack on Titan',
    long_description=readme,
    author='Colby Riddle',
    author_email='colbyriddle@gmail.com',
    url='https://github.com/IAmzColbz/AoT-Minigame',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)