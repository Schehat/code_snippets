class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@outlook.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):

    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lan):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)  # also possible
        self.prog_lan = prog_lan


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"===> {emp.fullname()}")


dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Test", "Employee", 60000, "Java")

mgr1 = Manager("Sue", "Smith", 90000, [dev_1])
mgr1.add_emp(dev_2)
mgr1.remove_emp(dev_1)
print("employee list:")
mgr1.print_emps()
print()

print(f"mgr1 is instance of Manager? {isinstance(mgr1, Manager)}")
print(f"mgr1 is instance of Employee? {isinstance(mgr1, Employee)}")
print(f"mgr1 is instance of Developer? {isinstance(mgr1, Developer)}\n")

print(f"is Manager a subclass of Manager? {issubclass(Manager, Manager)}")
print(f"is Manager a subclass of Employee? {issubclass(Manager, Employee)}")
print(f"is Manager a subclass of Developer? {issubclass(Manager, Developer)}\n")

print(dev_1.email)
print(dev_1.prog_lan)

print(f"\npay: {dev_1.pay}")
dev_1.apply_raise()
print(f"pay after raise: {dev_1.pay}")
