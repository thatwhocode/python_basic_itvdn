from .main import Manager


class TestManager(Manager):
    pass


manager = TestManager("John" ,28, 32.5)
assert manager.team_get_details == "Current team was not initialized with any member"