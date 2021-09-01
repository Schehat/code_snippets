li = {"list": [1]}

# if key does not exist it will be created and 3 will be appended
# if key does exist it just appends 3
print(li.setdefault("list", []).append(3))
print(li["list"])
