#!/usr/bin/env python
"""
lambdata helper functions
"""

import pandas as pd
import numpy as np
import unittest
import math

TEST = pd.DataFrame(np.ones(10))

class DataSci:
    '''Contains useful functions for data science'''
    def sqrt(n):
        '''Takes any positive number and returns the square root '''
        return n ** 0.5

    def mean(nums):
        '''Takes a list of numbers and returns the mean'''
        return sum(nums) / len(nums)

    def variance(nums, sample=False):
        '''Takes a list of numbers and returns the variance of the list,
        for sample variance use "sample=True"'''
        if sample:
             return sum((x - mean(nums)) ** 2 for x in nums) / (len(nums) - 1)
        else:
            return sum((x - mean(nums)) ** 2 for x in nums) / len(nums)

    def stdev(nums):
        '''Takes a list of numbers and returns the standard deviation'''
        return sqrt(variance(nums))
  
    def zscore(n, nums):
        '''Input number and list, returns zscore'''
        return (n - mean(nums)) / stdev(nums)
  
    def find_outliers(nums, threshold=1):
        '''input list of numbers returns list of outliers
        , default threshold=1'''
        outliers = []
        for i in range(len(nums)):
            if abs(zscore(nums[i],nums)) > threshold:
                outliers.append(nums[i])
        return outliers

class TestMethods(unittest.TestCase, DataSci):
    def test_sqrt(self):
        self.assertEqual(DataSci.sqrt(100), math.sqrt(100))
    
    def test_mean(self):
        self.assertEqual(DataSci.mean([3,4]), 3.5)

if __name__ == '__main__':
    unittest.main()