# sort lists
li = [4, 5, 2, 1, 8, 6, 3, 7, 9]

s_li = sorted(li)  # not in place
r_li = sorted(li, reverse=True)
li.sort()  # inplace

print("sort list:")
print(f"1 - sorted: {s_li}")
print(f"2 - sorted reversed: {r_li}")
print(f"3 - sort: {li}\n")

# sort tuple
tu = (4, 5, 3, 6, 1, 9, 2, 8, 7)
tu = sorted(tu)  # tuple don't have sort method
print(f"sort tuple: {tu}")

# sort dictionary by keys
student = {"name": "Schehat", "age": 20, "subject": "cs"}
student = sorted(student)
print(f"sort dictionary: {student}")

# custom sorting by abs
li = [-6, -5, -4, 1, 2, 3]
li = sorted(li, key=abs)
print(f"custom sorting: {li}")


# sort attributes
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name, self.age, self.salary}"

    # this is possible
    # def __lt__(self, other):
    #     return self.age < other.age


e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 60000)

employees = [e1, e2, e3]
employees = sorted(employees, key=lambda e: e.age)
print(f"\nsort attributes: {employees}")
