class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # this allows to define a function but treat it like an attribute
    @property
    def email(self):
        return f"{self.first}.{self.last}@outlook.de"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

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
emp_1.fullname = "Corey Schafer"  # calls setter decorator

print(emp_1.first)
print(emp_1.email)  # email wont change automatically the first name to Jim

# after emp1_1.fullname method cant be used like a function
# & after property decorator cant handle like a function
# print(emp_1.fullname())
print(emp_1.fullname)

del emp_1.fullname  # calls delete decorator
