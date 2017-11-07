from unittest import TestCase
import os, sys

my_path = os.path.dirname(os.path.dirname(os.getcwd()))
print my_path
sys.path.insert(0, my_path)


from tcwpy import TCWMtx

mat_file = "example_matrix.mtx"

class TestTCWMtx(TestCase):
    def test_info(self):
        pass
        # self.fail()

    def test_load(self):

        mymatrix = TCWMtx()
        mymatrix.load(mat_file)

        print mymatrix.matrix.keys()

        # self.fail()

    def test_export(self):
        pass
        # self.fail()

    def test_value(self):
        pass
        # self.fail()

    def test_changevalue(self):
        pass
        # self.fail()
