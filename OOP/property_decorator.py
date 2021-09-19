class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # this allows to define a function but treat it like an attribute
    # only purpose is to not rewrite code if email would be an attribute but
    # if emp1.first = "bla" then email would not automatically adjust the value
    # and defining a function without the property decorator would mean not rewrite
    # all access of this variable and adding the paranthesis
    # Note: just define the function in the first place. OOP programming in python is
    # compared to java a mess
    @property
    def email(self):
        return f"{self.first}.{self.last}@outlook.de"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # add decorators on top of the property decorator
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

    @fullname.deleter
    def fullname(self):
        print("DELETE NAME!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")

# emp_1.first = "Jim"
# emp_1.fullname = "Corey Schafer"  # calls setter decorator

print(emp_1.first)
print(emp_1.email)

# using fullname as a function not possible after the property decorator was added
# print(emp_1.fullname())
print(emp_1.fullname)

del emp_1.fullname  # calls delete decorator
