from setuptools import find_packages, setup

setup(
    name='pycontent',
    version='0.1.0',
    description='Static Site Generator for PYTH courses',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=True,
    setup_requires=['wheel'],
)
