import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = f"postgresql+psycopg2://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASS")}@{os.environ.get("DB_HOST")}:{os.environ.get("DB_PORT")}/{os.environ.get("DB_NAME")}"
