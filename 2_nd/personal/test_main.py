from .main import Manager, Employee
man = Manager("John", 28, 1550.5)
rich = Employee("Richard", 25, 1250.5)
mark = Employee("Mark", 25, 1100.5)
def test_creation():
    assert man.name == "John"
    assert man.salary == 1550.5
    assert man.age == 28
    assert man.team ==[]

def test_adding_member():
    man.add_employee(rich)
    assert man.team.count(rich) == 1  
def test_removing_member():
    assert man.remove_employee(rich) == "Succesfully removed"
    assert man.team.count(rich) == 0
def test_removing_non_existing():
    if man.team == []:
        man.add_employee(rich)
    assert man.remove_employee(mark) == "There`s no such employee in team"
def test_get_details():
    if man.team == []:
        assert man.team_get_details() == "Current team was not initialized with any member"