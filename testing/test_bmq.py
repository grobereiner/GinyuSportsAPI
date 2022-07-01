import unittest
from server_BMQ.bmqueue import cache_name
from server_BMQ.bmqueue import BMQueue

class Test_BMQ(unittest.TestCase):

    def test_cache_name(self):
        self.assertEqual(cache_name(2), "cache2.csv")

    def test_bmq_methods(self):
        obj = BMQueue("testing/bmq_state/queue_init.json")
        obj.data["capacity"] = 3
        obj.data["front"] = 0
        obj.data["back"] = 2

        self.assertEqual(obj._BMQueue__next(2), 0)

        self.assertTrue(obj._BMQueue__is_full())
        obj.data["capacity"] = 4
        self.assertFalse(obj._BMQueue__is_full())

        obj.data["capacity"] = 0
        self.assertTrue(obj._BMQueue__is_full())

        obj.data["capacity"] = 3
        obj.data["front"] = -1
        obj.data["back"] = -1
        self.assertTrue(obj._BMQueue__is_empty())

        obj._BMQueue__resize()
        self.assertEqual(obj.data["capacity"], 6)



if __name__=="__main__":
    unittest.main()