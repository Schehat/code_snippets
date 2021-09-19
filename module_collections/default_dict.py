counts = {}
numbers = [1, 2, 3, 4, 2, 3, 4, 1, 5]

for key in numbers:
    if key not in counts:
        counts[key] = 0
    counts[key] += 1

# better way of doing this
# defaultdict automatically sets a value if key not in dict
# but be careful because method names differ
from collections import defaultdict

counts = defaultdict(lambda: 0)  # default value is 0

for key in numbers:
    counts[key] += 1

# output also different from regular dict
print(counts)

# if key does not exist it will be created and 3 will be appended
# if key does exist it just appends 3
li = {"list": [1]}
print(li.setdefault("list", []))
print(li.setdefault("not", []))

# "not" now exists in dict
print(li)
