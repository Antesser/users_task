#!/usr/bin/env python3


from orm import ORM


class GetUser:
    def get_user(self):
        ORM.get_users()


if __name__ == "__main__":
    all_users = GetUser()
    all_users.get_user()
