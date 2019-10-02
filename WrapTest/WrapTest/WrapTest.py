
import pathlib
import inspect
import sys
class Path(type(pathlib.Path())):
    @staticmethod
    def script_dir():
        print(inspect.stack()[1].filename)
        p = pathlib.Path(inspect.stack()[1].filename)
        return p.parent.resolve()

script_dir = pathlib.Path(__file__).parent.resolve()
print(open(str(Path.script_dir()/'testingPythonLib.py')).read())


import os
import shutil 
from unittest import TestCase
 
 
class PathTest(TestCase):
    def test_script_dir(self):
        expected = os.path.abspath(os.path.dirname(__file__))
        actual = str(Path.script_dir())
        self.assertEqual(expected, actual)
 
    def test_file_access(self):
        script_dir = os.path.abspath(os.path.dirname(__file__))
        subdir = os.path.join(script_dir, 'WrapTest')
        if Path(subdir).is_dir():
            shutil.rmtree(subdir)
        os.makedirs(subdir)
        file_path = str(Path(subdir)/'test.txt')
        content = '123'
        open(file_path, 'w').write(content)
        test_path = Path.script_dir()/subdir/'test.txt'
        actual = open(str(test_path)).read()
 
        self.assertEqual(content, actual)
 
print('\n'.join(sys.path))