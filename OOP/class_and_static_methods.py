class Employe:
    # class variable
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, name: str, pay):
        # instance variable
        self.name = name
        self.pay = pay
        self.email = name.lower() + '@gmail.com'

        # call the class method to increment the number of employees
        Employe.inc_no_of_emps()

    @classmethod
    def inc_no_of_emps(cls):
        cls.num_of_emps += 1

    @classmethod
    def dec_no_of_emps(cls):
        cls.num_of_emps -= 1

    @classmethod
    def get_current_no_of_emps(cls):
        return cls.num_of_emps

    def apply_raise(self):
        # self.pay = int(self.pay * Employe.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

    # sack the employee
    def sack(self):
        emp_name = self.name
        # call the class method to decrement the number of employees
        Employe.dec_no_of_emps()
        # remove the instance from the memory
        del self
        return f'{emp_name} has been sacked!'
    
    # make a static method that goes with the class, dont do anything unmannerly ignore is_workday function dont make is_workday funcation as static method
    @staticmethod
    def salary_range(desig: str):
        if desig == 'manager':
            return '50k - 100k'
        elif desig == 'developer':
            return '30k - 50k'
        else:
            return '10k - 30k'

print('No of employess:', Employe.get_current_no_of_emps())


emp_1 = Employe('Corey', 50000)
print('No of employess:', Employe.get_current_no_of_emps())
emp_2 = Employe('Test', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
# print(Employe.raise_amount)

# print(emp_1.__dict__)
# print(Employe.__dict__)

# Employe.raise_amount = 1.05
# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)
# print(Employe.raise_amount)

print('No of employess:', Employe.get_current_no_of_emps())

print(emp_1.sack())

print('No of employess:', Employe.get_current_no_of_emps())

print(Employe.salary_range('manager'))