import unittest
from foobarqix import FooBarQix

class TestFooBarQix(unittest.TestCase):
    def setUp(self):
        self.testClass = FooBarQix

    def test_convertor(self):
        foo_bar_qix_object = self.testClass()
        assert foo_bar_qix_object.convertor(50) == "BarBar"
        assert foo_bar_qix_object.convertor(75) == "FooBarQixBar"
        assert foo_bar_qix_object.convertor(100) == "Bar"
        assert foo_bar_qix_object.convertor(46) == "46"

    def test_range_convertor(self):
        start_point = 1
        end_point = 100
        foo_bar_qix_object = self.testClass()
        results = foo_bar_qix_object.range_convertor(start_point, end_point)
        expectations_file = open('expectations.txt','r')
        expectations = expectations_file.readlines()
        expectations_file.close()
        for i in range(start_point, end_point + 1):
            current_index = i
            assert results[i - 1] == expectations[i - 1].strip()

if __name__ == '__main__':
    unittest.main()

