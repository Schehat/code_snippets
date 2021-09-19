# list can be iterated because they return a iterable from the __iter__ method,
# but is not an iterator, due to no __next__ method
# Note: generators are special iterators.
# Every generator is an iterator but not every iterator is a generator

nums = [1, 2, 3]

# i_nums = nums.__iter_-()
i_nums = iter(nums)  # this way better

print(i_nums)
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))

# a for loop basically creates an iterator and calls next until StopIteration exception
# something like that:
while True:
    try:
        x = next(i_nums)
        print(x)
    except StopIteration:
        break


# create own range class which is an iterator and can be iterated
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val


nums = MyRange(1, 10)
print("\nclass:")
# using next(nums) instead of a loop also possible
for i in nums:
    print(i)


# create generator like the class
def my_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


print("\ngenerator:")
nums = my_range(1, 10)
# for loop also possible
print(next(nums))
print(next(nums))
print(next(nums))
