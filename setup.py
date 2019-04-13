from setuptools import setup

setup(
    name='SnapshotAlyzer',
    version='0.1',
    author ="Iclert Justilien",
    author_email="iclert@gmail.com",
    description="SnapshotAlyzer is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/purelife321/snapshotalyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',



)
