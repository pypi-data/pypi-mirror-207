from setuptools import find_packages, setup


setup(
    name='Pypicor',
    version='1.0.4',
    description='Python package with helpful things to use the Epicor API',
    packages=find_packages(),
    install_requires=['requests >= 2.29.0', 'pandas >= 2.0.1','numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)