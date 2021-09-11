class Person:
    pass


p = Person()

# # dynamically add attributes. Really do not do this
# p.first_name = "A"
# p.last_name = "B"

# print(p.first_name, p.last_name)

# first_key = "first"
# first_value = "A"

# setattr(p, first_key, first_value)
# value = getattr(p, first_key)
# print(p.first, value)

# can be useful to parse attributes trough a dict
person_info = {"first": "Schehat", "last": "Abdel Kader"}
for key, item in person_info.items():
    setattr(p, key, item)

for key in person_info.keys():
    print(getattr(p, key))
