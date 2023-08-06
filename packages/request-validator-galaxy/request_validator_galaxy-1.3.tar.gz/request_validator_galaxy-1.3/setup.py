from setuptools import setup, find_packages


setup(
    name='request_validator_galaxy',
    version='1.3',
    license='',
    author="Preetam Pawar",
    author_email='preetam.pawar@galaxyweblinks.in',
    packages=find_packages('pk_src'),
    package_dir={'': 'pk_src'},
    url='',
    keywords='galaxy project',
    install_requires=[
          'flask',
      ],

)
