
from setuptools import setup, find_packages
 
setup(name='pathology',
      version='0.1',
      url='https://github.com/the-gigi/pathology',
      license='MIT',
      author='Gigi Sayfan',
      author_email='the.gigi@gmail.com',
      description='Add static script_dir() method to Path',
      packages=find_packages(exclude=['tests']),
      long_description=open(str(Path.script_dir()/'testingPythonLib.py').read(),
      zip_safe=False)
 
