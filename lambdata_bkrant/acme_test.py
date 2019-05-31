#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_explode(self):
        """Test explode method"""
        prod = Product('Test Product', flammability=3, weight=10)
        self.assertEqual(prod.explode(), print("...boom!"))


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are accurate"""
    def test_default_num_products(self):
        """Tests that default number of products is 30."""
        self.assertEqual(len(generate_products()), 30)


if __name__ == '__main__':
    unittest.main()
