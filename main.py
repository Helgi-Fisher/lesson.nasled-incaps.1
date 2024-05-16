class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level):
        self.__access_level = access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.__users = []

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user):
        self.__users.remove(user)

    def get_users(self):
        return self.__users


# Example Usage
user1 = User(1, "Alice")
user2 = User(2, "Bob")
admin = Admin(100, "Admin")

admin.add_user(user1)
admin.add_user(user2)
print("Admin Users:")
for user in admin.get_users():
    print(f"ID: {user.get_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")
