from setuptools import setup

setup(
    name="vkolev-pipeline",
    description="Simple gaia python pipeline example",
    packages=['pipeline'],
    author="vkolev",
    author_email="vkolev@pm.me",
    install_requires=[
        'gaiasdk>=0.0.16',
        'requests',
    ])
