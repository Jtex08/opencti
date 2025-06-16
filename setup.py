from setuptools import setup, find_packages

setup(
    name='bayesian-security-sim',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'typer[all]',
        'numpy',
        'pandas',
        'matplotlib',
        'scipy',
        'seaborn',
        'rich',
        'arviz'
    ],
    entry_points={
        'console_scripts': [
            'bayesim=main:app'
        ]
    },
    author='Your Name',
    description='Bayesian Security Simulation CLI for vulnerability and risk modeling',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)
