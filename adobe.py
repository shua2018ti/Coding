"""
Given an array of numbers nums, return an array of numbers products where products[i] is the product
of all nums[j] where j != i. Do this without using divide
"""

nums = [2, 3, 4, 5, 2] # products = [120, 80, 60, 48, 128]

def get_products(nums):
    prod_so_far = 1
    left = []
    for num in nums:
        left.append(prod_so_far)
        prod_so_far *= num
    prod_so_far = 1
    right = []
    for idx in range(len(nums) - 1, -1, -1):
        right.insert(0, prod_so_far)
        prod_so_far *= nums[idx]
    products = []
    for num1, num2 in zip(left, right):
        products.append(num1 * num2)
    return products

print(get_products(nums))
