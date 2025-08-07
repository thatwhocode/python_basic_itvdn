from typing import List
from random import randint
class Student():
    def __init__(self, name: str, grades : List[int] ) -> None:
        self.name = name
        self._grades = grades
        self.__id =  randint(1, 10000)
    def get_id(self):
        return self.__id
    def describe(self):
        print(f"Student id id {self.__id}, student name is {self.name},and student grades are ", *self._grades)
    def add_grade(self, grade) -> None:    
            if grade>0:
                self._grades.append(grade)
            else:
                print("Grades can not be negative")
    def get_average_grade(self):
            avg = sum(self._grades)/(len(self._grades))
            return(int(avg))
    def get_details(self):
            return f"Student name is {self.name}, student id is {  self.get_id()}, average grades(rounded) {self.get_average_grade()}"
        


if __name__ =='__main__':
    stud = Student("Stanislav", [3,4,5])
    print (stud.get_average_grade())
    print(stud.get_details())