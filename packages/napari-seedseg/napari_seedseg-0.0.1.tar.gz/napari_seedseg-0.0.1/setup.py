from setuptools import setup, find_packages


setup(
    name='napari_seedseg',
    version='0.0.1',
    license='BSD-3',
    author="Reza Akbarian Bafghi",
    author_email='reza.akb98@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/rezaakb/napari-seedseg',
    keywords='example project',
    install_requires=[
          'napari',
          'numpy',
          'magicgui',
          'qtpy',
          'opencv-python-headless',
          'scikit-image>=0.19.3',
      ],

)