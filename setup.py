import os
import platform
import subprocess

from skbuild import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

pysurvive_path = this_directory + '/bindings/python/pysurvive/'
cmake_args = ['-DPYTHON_GENERATED_DIR="' + pysurvive_path + '"',
              "-DDOWNLOAD_EIGEN=ON",
              "-DUSE_EIGEN=ON",
              "-DBUILD_APPLICATIONS=OFF",
              "-DLIB_INSTALL_DIR=bindings/python/pysurvive/"]

if platform.system() != 'Windows':
    cmake_args.append('-DUSE_EIGEN=ON')

description = """Libsurvive is a set of tools and libraries that enable 6 DoF tracking
 on lighthouse and vive based systems that is completely open source and can run on
 any device. It currently supports both SteamVR 1.0 and SteamVR 2.0 generation of
 devices and should support any tracked object commercially available."""

setup(name='pysurvive',
      version="v0.0.1",
      long_description=long_description,
      long_description_content_type='text/markdown',
      description=description,
      url='https://github.com/cntools/libsurvive',
      packages=['pysurvive'],
      package_dir={'pysurvive': 'bindings/python/pysurvive'},
      package_data={'pysurvive': ['images/*']},
      install_requires=[],
      include_package_data=False,
      license='MIT',
      cmake_args=cmake_args
      )
