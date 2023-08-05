from setuptools import setup, find_packages


setup(
    name='first_pypi_proj',
    version='1',
    license='MIT',
    author="Shreyas Labh",
    author_email='shreyas.labh@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/shreyaslabh/first_pypi_proj',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)
