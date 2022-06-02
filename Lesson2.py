class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return("{} {}".format(self.first,self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
emp_1 = Employee("Corey" , "Schafer" , 50000)
emp_2 = Employee("Test" , "User" , 60000)
#line below adds the attribute of raise_amount to only emp_1
emp_1.raise_amount = 1.05


print(Employee.raise_amount)
print(Employee.num_of_emps)