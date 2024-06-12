from setuptools import setup, find_packages

setup(
    name='quantum_bell_api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    entry_points={},
    url='https://github.com/LBacciottini/quantum_bell_api',
    author='Leonardo Bacciottini',
    author_email='baccio.leonardo@gmail.com',
    description='A package implementing quantum algebraic operations on Bell diagonal states.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)
