#!/usr/bin/env python3
from models import User
from orm import ORM


class TableCreation:
    def create(self):
        ORM.create_table()
