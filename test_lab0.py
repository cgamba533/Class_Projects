import unittest
from lab0 import *

class testCases(unittest.TestCase):

    def test_getPrice(self):
        watch = Product("Watch", 5, 250, 1200)
        price = watch.get_price()
        self.assertEqual(price, 1250)

    def test_make_purchase(self):
        wallet = 1600
        watch = Product("watch", 5, 175, wallet)
        purchase = watch.make_purchase(2)
        self.assertEqual(purchase, 1250)

    def test_make_purchase_2(self):
        wallet = 800
        tee_shirt = Product("Tee Shirt", 8, 10, wallet)
        with self.assertRaises(ValueError):
            tee_shirt.make_purchase(200)

    def test_Converter(self):
        test = Converter(6, "inches")
        test.convert()
        result = test.feet()
        self.assertEqual(result, 0.5)

    def test_Converter_2(self):
        test = Converter(3, "inches")
        test.convert()
        result = test.inches()
        self.assertEqual(result, 3)

