from typing import List, Optional
class Employee:
    def __init__(self, name: str, age:int, salary:float) -> None:
        self.name = name
        self.age = age 
        self.salary = salary
    
    def get_details(self)->str:
        return(f" Employee {self.name} is {self.age} years old, and makes{self.salary} a month")

class Manager(Employee):
    def __init__(self, name: str , age:int, salary: float, team:Optional[List[Employee]] = None) -> None:
        super().__init__(name, age, salary)
        self.team = team if team is not None else []
    def add_employee(self, employee: Employee) -> None:
        if employee:
            self.team.append(employee)
    def remove_employee(self, employee) -> str:
        if self.team == []:
            return("Team list is empty right now")
        else:
            if employee in self.team:
                self.team.remove(employee)
                return "Succesfully removed"
            else:
                return "There`s no such employee in team"
    def team_get_details(self):
        if self.team == []:
            return("Current team was not initialized with any member")
        else:
            for employee in self.team:
                employee.get_details()
        