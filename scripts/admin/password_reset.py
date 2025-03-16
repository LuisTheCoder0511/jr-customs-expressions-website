from scripts.database import db_passwords
from scripts.database.oracle import database

db_passwords.__drop_table__()
db_passwords.__create_table__()
database.__close__()
