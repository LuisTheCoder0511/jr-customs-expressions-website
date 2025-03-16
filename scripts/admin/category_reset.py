from scripts.database import db_categories
from scripts.database.oracle import database

db_categories.__drop_table__()
db_categories.__create_table__()
database.__close__()
