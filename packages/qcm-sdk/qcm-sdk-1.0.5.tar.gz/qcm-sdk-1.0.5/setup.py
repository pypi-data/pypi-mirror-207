from setuptools import setup

setup(
    name='qcm-sdk',
    version='1.0.5',
    description='Python SDK for interacting with QCM API',
    author='Chetan N',
    author_email='chetan@quoqo.com',
    packages=['qcm_sdk'],
    install_requires=[
        'requests',
    ],
)

