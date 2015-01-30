import unittest
from tarea3 import *

class TestSuite(unittest.TestCase):
	def test_CarJustLeft(self):
		reservations = []
		for i in range(9):
			reservations.append([8,12])
		reservations.append([8,10])
		self.assertEqual(True, marzullo(reservations, 10, 12))
			
	def test_ParkingTotallyFull
		reservations = []
		for i in range(10):
			reservations.append([6,18])
		self.assertEqual(False, marzullo(reservations, 8, 12))

