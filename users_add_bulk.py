#!/usr/bin/env python3

import itertools
import random
from datetime import date, timedelta

from faker import Faker

from orm import ORM

fake = Faker("ru_RU")


class AddBulk:
    def add_bulk(self):
        chunk_len = 10000
        all_users = self.generate_users()
        all_users.extend(self.generate_f_users())
        bulk_data = split_bulk(all_users, chunk_len)
        for data in bulk_data:
            ORM.add_bulk(data)

    cyrilic_dict = {
        "Ь": "",
        "ь": "",
        "Ъ": "",
        "ъ": "",
        "А": "A",
        "а": "a",
        "Б": "B",
        "б": "b",
        "В": "V",
        "в": "v",
        "Г": "G",
        "г": "g",
        "Д": "D",
        "д": "d",
        "Е": "E",
        "е": "e",
        "Ё": "Yo",
        "ё": "yo",
        "Ж": "Zh",
        "ж": "zh",
        "З": "Z",
        "з": "z",
        "И": "I",
        "и": "i",
        "Й": "Y",
        "й": "y",
        "К": "K",
        "к": "k",
        "Л": "L",
        "л": "l",
        "М": "M",
        "м": "m",
        "Н": "N",
        "н": "n",
        "О": "O",
        "о": "o",
        "П": "P",
        "п": "p",
        "Р": "R",
        "р": "r",
        "С": "S",
        "с": "s",
        "Т": "T",
        "т": "t",
        "У": "U",
        "у": "u",
        "Ф": "F",
        "ф": "f",
        "Х": "H",
        "х": "h",
        "Ц": "Ts",
        "ц": "ts",
        "Ч": "Ch",
        "ч": "ch",
        "Ш": "Sh",
        "ш": "sh",
        "Щ": "Sch",
        "щ": "sch",
        "Ы": "Yi",
        "ы": "yi",
        "Э": "E",
        "э": "e",
        "Ю": "Yu",
        "ю": "yu",
        "Я": "Ya",
        "я": "ya",
    }

    def generate_users(self):
        num_users = 1_000

        user_data = []
        table = str.maketrans(self.cyrilic_dict)
        for _ in range(num_users):
            users = {}
            users["sex"] = random.choice(["Male", "Female"])
            if users["sex"] == "Male":
                random_name = fake.name_male().translate(table)
            else:
                random_name = fake.name_female().translate(table)
            users["name"] = random_name
            users["date"] = str(
                date.today() - timedelta(days=random.randint(2, 365 * 100))
            )
            users["age"] = ""
            user_data.append(users)
        return user_data

    def generate_f_users(self):
        num_users = 100

        user_data = []
        table = str.maketrans(self.cyrilic_dict)
        for _ in range(num_users):
            users = {}
            users["sex"] = "Male"
            random_name = "F" + fake.name_male().translate(table)[1:]

            users["name"] = random_name
            users["date"] = str(
                date.today() - timedelta(days=random.randint(2, 365 * 100))
            )
            users["age"] = ""
            user_data.append(users)
        return user_data


# рекурсивно разбиваем нашу последовательность пользователей на требуемое количество частей
def split_bulk(seq, *args):
    if args:
        n, *args = args
        return [split_bulk(c, *args) for c in chunks(seq, n)]
    return list(seq)

# используем ленивый генератор для экономия памяти
def chunks(seq, n):
    it = iter(seq)
    while True:
        chunk = list(itertools.islice(it, n))
        if len(chunk) == 0:
            break
        yield chunk


# if __name__ == "__main__":
#     new_employee = AddBulk()
#     new_employee.add_bulk()
