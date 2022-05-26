from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

setup(
    name='tuner',
    version='0.0.2-alpha1',
    description='auto tuning machiner learning',
    long_description=readme,
    license=license,
    author='FUKUDA Yutaro',
    author_email='sktnkysh+dev@gmail.com',
    url='https://github.com/sktnkysh/tuner',
    packages=find_packages(),
    entry_points={
        'console_scripts':
        ['format-dataset=tuner.scripts.format_dataset:main', 'toon=tuner.scripts.toon:main']
    },
    install_requires=[
        'numpy',
        'pandas',
        'Pillow',
        'h5py',
        'tensorflow==2.7.2',
        'keras',
    ],
    dependency_links=[
        'git+https://github.com/hyperopt/hyperopt.git',
        'git+https://github.com/mdbloice/Augmentor.git',
        'git+https://github.com/maxpumperla/hyperas.git'
    ])
