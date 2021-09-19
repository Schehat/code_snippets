import itertools
import operator
import os

data = [100, 200, 300, 400]

# generate indexes quick with count method. Count can go to infinity
daily_data = list(zip(itertools.count(), data))
print("count:")
print(daily_data)
daily_data = list(zip(itertools.count(start=5, step=5), data))
print(daily_data)

# do not use itertools.count otherwise goes to infinity
daily_data = list(itertools.zip_longest(range(10), data))
print("\nzip_longest:")
print(daily_data)

# cycle as the name suggest cycles trough in iterator
daily_data = itertools.cycle(("On", "Off"))
print("\ncycle:")
for i in range(5):
    print(next(daily_data))

# similar to map() but can use tuples instead of two separate iterables
squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2)])
print("\nstarmap:")
print(list(squares))

letters = ["a", "b", "c", "d"]
# 2 means all combinations of 2 values
# in combinations & permutations repeats are not included like ("a", "a")
result = itertools.combinations(letters, 2)
print("\ncombinations:")
for i in result:
    print(i)

result = itertools.permutations(letters, 2)
print("\npermutations:")
for i in result:
    print(i)

# allows repeats. Also possible
result = itertools.combinations_with_replacement(letters, 2)
print("\ncombinations_with_replacement:")
for i in result:
    print(i)

# cartesian product includes repeats
digits = [1, 2, 3, 4]
# repeat means all variations 0f 4 values including repetition
result = itertools.product(digits, repeat=2)
print("\nproduct:")
for i in result:
    print(i)

# chains multiple objects which can be iterated trough
combined = itertools.chain(letters, digits)
print("\ncombined:")
for i in combined:
    print(i)

# arguments - 1: iterable, 2: stopping point
# if 4 parameters given: 1: still iterable, 2: starting point, 3: stopping point, 4: step
result = itertools.islice(range(10), 1, 5, 2)
print("\nislice:")
for i in result:
    print(i)

# example of islice using a file. File are iterables too
os.chdir(os.path.dirname(__file__))
print("\nislice with a file:")
with open("data.txt", "r") as file:
    header = itertools.islice(file, 3)

    for i in header:
        print(i, end="")

# compress returns an iterable if the list had a corresponding True value
selectors = [1, 1, 0, 1]
result = itertools.compress(letters, selectors)
print("\ncompress:")
for i in result:
    print(i)


def lt_2(x):
    return x > 2


result = filter(lt_2, digits)
print("\nfilter similar to compress but evaluating by a function:")
for i in result:
    print(i)

result = itertools.filterfalse(lt_2, digits)
print("\nfilterfalse like filer but takes false:")
for i in result:
    print(i)

# itertools.dropwhile & itertools.takeaway are similar but
# dropwhile drops elements which turn out false until it evaluates a true value
# then the iterable will be returned and every element after this true element are included.
# takeaway returns iterable of true values until it evaluates a false value and drops every element
# after the false value (the first false value included) and only includes the true value

# operator optional by default it is plus
result = itertools.accumulate(digits, operator.mul)
print("\naccumulate")
for i in result:
    print(i)
