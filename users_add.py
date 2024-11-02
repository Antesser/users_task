import sys

from orm import ORM

name = sys.argv[1]
date = sys.argv[2]
sex = sys.argv[3]


class AddUser:
    def add_user(self):
        ORM.insert_users(name, date, sex)


if __name__ == "__main__":
    new_employee = AddUser()
    new_employee.add_user()
