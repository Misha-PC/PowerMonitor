from .connector import Database
from Config import Configuration


db = Database(
    dbname=Configuration.DB_NAME,
    user=Configuration.DB_USER,
    password=Configuration.DB_PASS,
    host=Configuration.DB_HOST
)