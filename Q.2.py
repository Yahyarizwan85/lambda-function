# Question 2: the reduce function to find the product of the double numbers

from functools import reduce

nums = [2, 4, 6, 8, 10]
multiply_num = list(map(lambda x: x * 2, nums))
product = reduce(lambda x, y: x * y, multiply_num)
print(print(f"{multiply_num} is a product of {product}"))
