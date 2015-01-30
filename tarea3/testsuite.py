import unittest
from tarea3 import *

class TestSuite(unittest.TestCase):
	def test_CarJustLeft(self):
		reservations = []
		for i in range(9):
			reservations.append([8,12])
		reservations.append([8,10])
		self.assertEqual(True, marzullo(reservations, 10, 12))
			
	def test_ParkingTotallyFull(self):
		reservations = []
		for i in range(10):
			reservations.append([6,18])
		self.assertEqual(False, marzullo(reservations, 8, 12))

	def test_ParkingEmpty(self):
		reservations = []
		self.assertEqual(True, marzullo(reservations, 8, 12))

	def test_PerfectlyFit(self):
		reservations = []
		for i in range(10):
			reservations.append([8,10])
			reservations.append([12,14])
		for i in range(9):
			reservations.append([10,12])
		self.assertEqual(True, marzullo(reservations, 10, 12))

	def test_OnlyParkingLotAvailableAllDay(self):
		reservations = []
		for i in range(10):
			reservations.append([6,10])
			reservations.append([12,18])
		for i in range(9):
			reservations.append([10,12])
		self.assertEqual(True, marzullo(reservations, 10, 12))

	def test_ReservingAllDayEmptyParking(self):
		reservations = []
		self.assertEqual(True, marzullo(reservations, 6, 18))

	def test_ReservingAllDayNotEmptyParking(self):
		reservations = []
		reservations.append([6,7])
		self.assertEqual(False, marzullo(reservations, 6, 18))