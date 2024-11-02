#!/usr/bin/env python3
from models import User
from orm import ORM


class TableCreation:
    def create(self):
        ORM.create_table()


if __name__ == "__main__":
    new_employee = TableCreation()
    new_employee.create()
