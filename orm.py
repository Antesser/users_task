from database import Base, engine


class ORM:
    @staticmethod
    def create_table():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
