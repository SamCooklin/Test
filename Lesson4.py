class Employee:
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        

    def fullname(self):
        return("{} {}".format(self.first,self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.1
    #line below is there because too many arguments to send to Employee
    def __init__(self, first, last, pay, prog_lang):
        #line below passes all of these vars to Employee to deal with so code isn't repeated
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang


dev_1 = Developer("Corey" , "Schafer" , 50000 , "Python")
dev_2 = Developer("Test" , "User" , 60000 , "Java")

print(dev_1.prog_lang)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)




