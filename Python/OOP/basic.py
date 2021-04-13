class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

        # Conditional Attributes
        if salary < 0:
            self.salary = "Invalid Salary Less than Zero"
        else:
            salary = salary


ahsanulhaq = Employee('AHSAN UL HAQ', 'IT ASSISTANT', 104000)
kashif = Employee('Kashif Hanif', 'Meter Reader Supervisor', -25000)
mustfeez = Employee('Mustfeez Ur Rehman', 'Meter Reader', 18000)

print("IT Assistant Name :", ahsanulhaq.name)
print("Meter Reader Supervisor Salary:", kashif.salary)
print("Utility Meter Reader Designation:", mustfeez.designation)
