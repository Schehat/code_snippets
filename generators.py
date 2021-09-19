def square_numbers(nums):
    for i in nums:
        yield i * i


# generator does not have result in space
my_nums = square_numbers(range(1, 6))

# generator comprehension also possible then yield not necessary
# my_nums = (n * n for n in range(1, 6))

print(my_nums)

# print(list(my_nums))  # consumes iterations of generator
# print(next(my_nums))  # is a 1-step iteration, here 5 iterations possible

# iterate trough the generator
for num in my_nums:
    print(num)
