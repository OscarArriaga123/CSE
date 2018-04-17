class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, job, tired, name):
        super(Employee, self).__init__(name, 'age',)
        self.job = job
        self.tired = tired

    def home(self):
        print("When the Employee gets home he's %s" % self.tired)


class Programmer(Employee):
    def __init__(self, fast, job, name):
        super(Programmer, self).__init__(job, name, 'tired')
        self.fast = fast

    def computer(self):
        print("The programmer is an expert on typing %s on a computer" % self.fast)