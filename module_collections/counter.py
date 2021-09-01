from collections import Counter

counts = {}
numbers = [1, 2, 3, 4, 2, 3, 4, 1, 5]

for key in numbers:
    if key not in counts:
        counts[key] = 0
    counts[key] += 1

# better solution
numbers = [1, 2, 3, 4, 2, 3, 4, 1, 5]

counter = Counter(numbers)
print(counter)
counter = dict(counter)
print(counter)
