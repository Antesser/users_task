#!/usr/bin/env python3

import sys
from create_table import TableCreation
from users import User



mode = sys.argv[1]


class Start:
    user = User()
    def operating_mode(self, mode):
        match mode:
            case "1":
                new_employee = TableCreation()
                new_employee.create()
            case "2":
                name, date, sex = sys.argv[2], sys.argv[3], sys.argv[4]
                self.user.add_user(name, date, sex)
            case "3":
                self.user.get_user()
            case "4":
                self.user.add_bulk()
            case "5":
                self.user.get_f_user()


if __name__ == "__main__":
    new_employee = Start()
    new_employee.operating_mode(mode)
