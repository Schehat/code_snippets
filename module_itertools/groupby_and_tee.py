import itertools


def get_state(person):
    return person["state"]


people = [
    {"name": "John Doe", "city": "Gotham", "state": "NY"},
    {"name": "Jane Doe", "city": "Kings Landing", "state": "NY"},
    {"name": "Corey Schafer", "city": "Boulder", "state": "CO"},
    {"name": "Al Einstein", "city": "Denver", "state": "CO"},
    {"name": "John Henry", "city": "Hinton", "state": "WV"},
    {"name": "Randy Moss", "city": "Rand", "state": "WV"},
    {"name": "Nicole K", "city": "Asheville", "state": "NC"},
    {"name": "Jim Doe", "city": "Charlotte", "state": "NC"},
    {"name": "Jane Taylor", "city": "Faketown", "state": "NC"},
]

# groupby goes through an iterable and groups values based on a key and then returns a tuple.
# The tuple consists of the key the items got grouped & second value is an iterator containing all
# items grouped by that key
# Note: it is required that the list of dicts are sorted by the key values. So there are blocks
# items which are coming from the same state as shown in the above list
person_group = itertools.groupby(people, get_state)

# tee is used to copy. Can make as many copies as we want
# Note: after the method the original iterator should not be used
copy1, copy2 = itertools.tee(person_group)

for key, group in person_group:
    # print(key, len(list(group)))
    print(key)
    for person in group:
        print(person)
    print()
