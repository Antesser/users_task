from datetime import datetime
from sqlalchemy import select
from database import Base, engine, session_factory
from models import User


class ORM:
    @staticmethod
    def create_table():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_users(name, date, sex):
        with session_factory() as session:
            new_user = User(
                full_name=name,
                birth_date=date,
                sex=sex,
                age=calculate_age(date),
            )
            session.add(new_user)
            # flush отправляет запрос в базу данных
            # после flush пользователь получает первичный ключ id, который отдала БД
            session.flush()
            session.commit()

    @staticmethod
    def get_users():
        result = []
        with session_factory() as session:
            users = session.query(User).order_by(User.full_name).all()
            for user in users:
                result.append(
                    f"{user.full_name}, {user.birth_date}, {user.sex}, {user.age}"
                )
        print(result)
        return result


def calculate_age(date):
    try:
        birthdate = datetime.fromisoformat(date)
    except ValueError:
        # проверяем на високосный год
        _, month, day = date.split("-")
        if month == "02" and day == "29":
            date = date[:-1] + "8"
            birthdate = datetime.fromisoformat(date)
        else:
            raise ValueError("Check if inputed date is correct")
    today = datetime.now().date()
    age = (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )
    return age
