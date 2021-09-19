class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@outlook.com"

        Employee.num_of_emps += 1  # more logical using Employee than self

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        # using self.raise_amount more flexible than Employee.raise_amount
        # only logical if the variable can differ from other instances
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("Schehat", "Abdel_Kader", 100)
emp2 = Employee("John", "Miller", 50000)

print(f"full name: {emp1.fullname()}")

print(f"\npay: {emp1.pay}")
emp1.apply_raise()
print(f"pay after raise: {emp1.pay}")

Employee.raise_amount = 1.05

print("\nchange of raise amount with the class name Employee")
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print("\nEmployee has class variable raise_amount")
print(Employee.__dict__)
print("\nemp1 doesent have variable raise_amount")
print(emp1.__dict__)

emp1.raise_amount = 1.06  # only changes for emp1

print("\nchange of raise amount with the class instance emp1")
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print("\nafter that emp1 has a unique instance variable raise_amount")
print(emp1.__dict__)

# big problem nothing is stopping us to do it again and change
# the variable of the class with an instance
emp1.num_of_emps = 10
print(f"\nbig problem it is n: {emp1.num_of_emps}")
