from setuptools import setup

setup(
    name='asa-tools',
    version='0.1.1',
    py_modules=['turn2release'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        asa=turn2release:cli
    ''',
)