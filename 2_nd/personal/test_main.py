from .main import Manager


class TestManager(Manager):
    pass


manager = TestManager("John" ,28, 32.5)
test = manager.team_get_details()
assert test == "Current team was not initialized with any member"