#!/usr/bin/env python3

from orm import ORM


class GetFUser:
    def get_f_user(self):
        ORM.get_f_users()


# if __name__ == "__main__":
#     all_users = GetFUser()
#     all_users.get_f_user()
