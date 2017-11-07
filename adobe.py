"""
Given an array of numbers nums, return an array of numbers products where products[i] is the product
of all nums[j] where j != i. Do this without using divide
"""

nums = [2, 3, 4, 5, 2] # products = [120, 80, 60, 48, 128]

def get_products(nums):
    prod_so_far = 1
    left = []
    for idx, num in enumerate(nums):
