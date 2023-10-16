from multilevel.employee import Employee
from multilevel.person import Person


class Teacher(Employee, Person):
    def teach(self):
        return "teaching..."

