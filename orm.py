import time

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
            new_user = User(full_name=name, birth_date=date, sex=sex)
            session.add(new_user)
            # flush отправляет запрос в базу данных
            # после flush пользователь получает первичный ключ id, который отдала БД
            session.flush()
            session.commit()

    @staticmethod
    def get_users():
        with session_factory() as session:
            users = session.query(User).order_by(User.full_name).all()
        return users

    @staticmethod
    def add_bulk(bulk_data):
        with session_factory() as session:
            for data in bulk_data:
                new_user = User(
                    full_name=data.get("name"),
                    birth_date=data.get("date"),
                    sex=data.get("sex"),
                )
                session.add(new_user)
            session.flush()
            session.commit()

    @staticmethod
    def get_f_users():
        result = []
        start_time = time.time()
        with session_factory() as session:
            users = (
                session.query(User)
                .filter(User.full_name.startswith("F"), User.sex == "Male")
                .all()
            )
            for user in users:
                result.append(
                    f"{user.full_name}, {user.birth_date}, {user.sex}"
                )
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Execution time was {round(execution_time,4)} sec")
