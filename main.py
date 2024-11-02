#!/usr/bin/env python3

import sys
from users_create import TableCreation
from users_add import AddUser
from users_get import GetUser
from users_add_bulk import AddBulk
from users_f_get import GetFUser


mode = sys.argv[1]


class Start:
    def operating_mode(self, mode, *args):
        match mode:
            case "1":
                new_employee = TableCreation()
                new_employee.create()
            case "2":
                name, date, sex = sys.argv[2], sys.argv[3], sys.argv[4]
                new_employee = AddUser()
                new_employee.add_user(name, date, sex)
            case "3":
                all_users = GetUser()
                all_users.get_user()
            case "4":
                new_employee = AddBulk()
                new_employee.add_bulk()
            case "5":
                all_users = GetFUser()
                all_users.get_f_user()


if __name__ == "__main__":
    new_employee = Start()
    new_employee.operating_mode(mode)
