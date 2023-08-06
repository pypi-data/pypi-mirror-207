from setuptools import setup

setup(
    name='deepchecks-installer',
    version='0.1',
    py_modules=['cli'],
    package_data={'': ['*.sh']},
    install_requires=[
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'deepchecks-installer=cli:main',
        ],
    },
)