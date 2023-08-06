from setuptools import setup, find_packages

setup(
    name='gnnom',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/emblsaxs',
    license='MIR',
    author='Dima',
    author_email='dmitry.molodenskiy@embl-hamburg.de',
    description='Apply NNs for SAXS data analysis',
    download_url = 'https://github.com/emblsaxs/gnnom/archive/refs/tags/1.0.1.tar.gz',
    keywords = ['SAXS', 'NN', 'ML', 'AI'],
    classifiers=[],
)
