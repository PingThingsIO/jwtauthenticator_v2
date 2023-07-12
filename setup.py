from setuptools import setup

setup(
    name='jupyterhub-jwtauthenticator-v2',
    version='2.1.0',
    description='JSONWebToken Authenticator for JupyterHub',
    url='https://github.com/PingThingsIO/jwtauthenticator_v2',
    author='youngale-pingthings',
    author_email='alexander.young@pingthings.io',
    license='Apache 2.0',
    packages=['jwtauthenticator'],
    install_requires=[
        'jupyterhub',
        'pyjwt',
    ]
)
