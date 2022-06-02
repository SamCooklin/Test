class Employee:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'
  def fullname(self):
    return("{} {}".format(self.first,self.last))
    
emp_1 = Employee("Corey" , "Schafer" , 50000)
emp_2 = Employee("Test" , "User" , 60000)
print(emp_1.email)
print(emp_2.email)


#Line below use the {} as placeholders - probably better for a one time use only
print("{} {}".format(emp_1.first,emp_1.last))

#Line below uses the fullname function in the class
print(emp_2.fullname())