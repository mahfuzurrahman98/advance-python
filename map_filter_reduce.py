from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
sq_nums = list(map(lambda x: x ** 2, even_nums))
sum_sq_nums = reduce(lambda x, y: x + y, sq_nums)

print(sum_sq_nums)
