#!/usr/bin/env python
"""
Acme
"""

import random


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999+1)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            print('Not so stealable.')
        elif ratio < 1.0:
            print("Kinda stealable.")
        else:
            print("Very stealable!")

    def explode(self):
        fw = self.flammability*self.weight
        if fw < 10:
            print("...fizzle.")
        elif fw < 50:
            print("...boom!")
        else:
            print("...BABOOM!!")


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999+1)):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability, identifier=identifier)

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            print("That tickles.")
        elif self.weight < 15:
            print("Hey that hurt!")
        else:
            print("OUCH!")
