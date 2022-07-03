class User:

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def __repr__(self):
        return "User({0.user_id!r})".format(self)


users = [User(23), User(3), User(99)]
print(users)
from operator import attrgetter

print(sorted(users, key=attrgetter("user_id")))
sorted_user = sorted(users, key=lambda user: user.user_id)
print(sorted_user)

print(min(users, key=attrgetter("user_id")))
