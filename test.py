# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest
import pandas as pd
from baseplots import Plot1d
from baseplots import Plot2d

class TestPlot1d(unittest.TestCase):
    def setUp(self):
        data = pd.DataFrame()
        self.plot1d = Plot1d(data, "korktype")
        self.plot1d.read_data_file('test_data.csv')

    def test_initialization(self):
        self.assertEqual(self.plot1d.variable, 'korktype', 'incorrect variable name')

    def test_readdata(self):
        self.assertEqual(self.plot1d.df.shape[0], 21117, 'incorrect number of rows in df')

class TestPlot2d(unittest.TestCase):
    def setUp(self):
        data = pd.DataFrame()
        self.plot1d = Plot2d(data, ["korktype", "alkohol"])
        self.plot1d.read_data_file('test_data.csv')

    def test_initialization(self):
        self.assertEqual(self.plot1d.variable_list[0], 'korktype', 'incorrect variable name')

    def test_readdata(self):
        self.assertEqual(self.plot1d.df.shape[0], 21117, 'incorrect number of rows in df')


if __name__ == '__main__':
    unittest.main()
