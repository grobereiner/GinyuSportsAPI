import unittest
from server_ADMIN import scrap

class Testear(unittest.TestCase):
    def test_date_format(self):
        self.assertEqual(scrap.date_format("Fri 4 Mar"), '2022-03-04')

if __name__=="__main__":
    unittest.main()