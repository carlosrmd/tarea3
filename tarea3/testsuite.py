import unittest
from functions import compute_payment
from Tarifa import Tarifa
from datetime import datetime

class TestSuite(unittest.TestCase):
	def test_CarJustLeft(self):
		for i in range(9):
			
