#!/usr/bin/env python3
# import sys


# name = sys.argv[1]
# date = sys.argv[2]
# sex = sys.argv[3]

from orm import ORM
from models import User


class TableCreation:
    def create(self):
        ORM.create_table()


if __name__ == "__main__":
    new_employee = TableCreation()
    new_employee.create()
