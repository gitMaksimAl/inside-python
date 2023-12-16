import json
from pprint import pprint
from pathlib import Path

from Lesson_13.task2 import LevelError, AccessError


class User:

    def __init__(self, name: str, user_id: str, level: int):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self):
        return hash((self.name, self.user_id))

    def __repr__(self):
        return f"User('{self.name}', {self.user_id}, {self.level})"


class UserKeeper:

    def __init__(self):
        self._users = set()
        self._user = None

    def get_users_from_json(self, path_to_file: str):
        with open(path_to_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for user in data:
                self._users.add(User(user['name'], user['id'], user['level']))

    def enter(self, name: str, user_id: str):
        user = User(name, user_id, 0)
        for u in self._users:
            if u == user:
                self._user = u
                return u.level
        raise AccessError('Wrong name or id')

    def add_user(self, name: str, user_id: str, level: int):
        if self._user.level < level:
            raise LevelError('You do not have privileges for this user')
        user = User(name, user_id, level)
        self._users.add(user)
        return user

    def get_users(self) -> set:
        return self._users


if __name__ == "__main__":
    keeper = UserKeeper()
    keeper.get_users_from_json('./Lesson_8/users.json')
    print(f"You have access level: {keeper.enter('Maksim', '0000000001')}")
    keeper.add_user('Gavril', '00000032', 1)
