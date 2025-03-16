from scripts.database import db_accounts
from scripts.database.oracle import database

db_accounts.__drop_table__()
db_accounts.__create_table__()
database.__close__()
