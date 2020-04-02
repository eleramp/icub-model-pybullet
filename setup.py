import os
from setuptools import setup, find_packages

setup_py_dir = os.path.dirname(os.path.realpath(__file__))
need_files = []
datadir = "icub_model_pybullet"

hh = setup_py_dir + "/" + datadir

for root, dirs, files in os.walk(hh):
  for fn in files:
    ext = os.path.splitext(fn)[1][1:]
    if ext and ext in 'urdf sdf xml yaml stl ini dae'.split(
    ):
      fn = root + "/" + fn
      need_files.append(fn[1 + len(hh):])


setup(
  name="icub-model-pybullet",
  version="0.1",
  author="Diego Ferigo",
  author_email="diego.ferigo@iit.it",
  description="SDF iCub model for PyBullet",
  license="LGPL",
  platforms='any',
  python_requires='>=3.6',
  keywords="sdf icub models robot robotics humanoid simulation pybullet",
  packages=find_packages(),
  package_data={'icub_model_pybullet': need_files},
  url="https://github.com/diegoferigo/icub-model-pybullet",
)
