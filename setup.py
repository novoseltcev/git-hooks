from setuptools import setup

setup(
    entry_points={'console_scripts': [
        'commit-msg = commit-msg:main',
    ]}
)

