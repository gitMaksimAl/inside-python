import pytest

from Lesson_13.task3 import User, UserKeeper
from Lesson_13.task2 import AccessError, LevelError


@pytest.fixture
def user_data():
    return 'new', '0000101', 2


def test_add_user(user_data):
    keeper = UserKeeper()
    keeper.get_users_from_json('../Lesson_8/users.json')
    keeper.enter('Olga', '0000000004')
    assert keeper.add_user(*user_data)


def test_privilege(user_data):
    keeper = UserKeeper()
    keeper.get_users_from_json('../Lesson_8/users.json')
    keeper.enter('Maksim', '0000000001')
    with pytest.raises(LevelError):
        keeper.add_user(*user_data)


if __name__ == "__main__":
    pytest.main()
