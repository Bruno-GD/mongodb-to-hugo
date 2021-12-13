from setuptools import setup

setup(
    name='MoPyGo',
    version='1.0',
    description='Get MongoDB data & generate site with Hugo',
    author='Bruno Golomb Durán, Noelia Crespi Pomar',
    packages=['src'],
    install_requires=[
        "pymongo",
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib"
    ]
)