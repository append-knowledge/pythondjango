class Employee():
    company_name='IBM'
    def __init__(self,name,id,experience,salary):
        self.name=name
        self.id=id
        self.experience=experience
        self.salary=salary
        print(self.name,self.id,self.experience,self.salary,Employee.company_name)
    def __str__(self):
        return self.name + str(self.experience) +Employee.company_name

obj1=Employee('LIJO JOSE',678544,8,45000)
print(obj1)
