#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    np = num_products
    products = []
    # TODO - your code! Generate and add random products.
    for _ in range(1, num_products+1):
        rand_name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        rand_price = randint(5, 100)
        rand_weight = randint(5, 100)
        rand_flammability = uniform(0.0, 2.5)
        rand_product = Product(name=rand_name, price=rand_price,
                               weight=rand_weight,
                               flammability=rand_flammability)
        products.append(rand_product)
    return products


def inventory_report(products):
    pass  # TODO - your code! Loop over the products to calculate the report.
    names, prices, weights, flammabilities = [], [], [], []
    for i in range(len(products)):
        names.append(products[i].name)
        prices.append(products[i].price)
        weights.append(products[i].weight)
        flammabilities.append(products[i].flammability)
    Number_of_unique_product_names = len(set(names))
    avg_price = sum(prices)/len(prices)
    avg_weight = sum(weights)/len(weights)
    avg_flammability = sum(flammabilities)/len(flammabilities)
    print('Unique product names:', Number_of_unique_product_names)
    print('Average price:', avg_price)
    print('Average weight:', avg_weight)
    print('Average flammability:', avg_flammability)


if __name__ == '__main__':
    inventory_report(generate_products())
