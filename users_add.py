#!/usr/bin/env python3


from orm import ORM


class AddUser:
    def add_user(self, name, date, sex):
        ORM.insert_users(name, date, sex)


# if __name__ == "__main__":
#     new_employee = AddUser()
#     new_employee.add_user()
