def append_number_wrong(num, numbers=[]):
    numbers.append(num)
    print(num)
    print(numbers)


# behaves not like expected due to mutable parameteter
# the function share the same list
print("wrong:")
append_number_wrong(1)
append_number_wrong(2)


# always use immutable data structure
def append_number_correct(num, numbers=None):
    numbers = []
    numbers.append(num)
    print(num)
    print(numbers)


print("\ncorrect:")
append_number_correct(1)
append_number_correct(2)
