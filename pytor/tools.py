import sqlite3
from config import DBConfig


def run_query(*query):
    with sqlite3.connect(DBConfig.path) as conn:
        cur = conn.cursor()
        return list(cur.execute(*query))

def ensure_tables():
    # known nodes
    tbls = run_query(
        """SELECT name FROM sqlite_master
           WHERE type='table'
           ORDER BY name;"""
    )

    print([t for t in tbls])

def drop_table(table_name):
    return run_query("""DROP TABLE IF EXISTS {}""".format(table_name))

def create_table(table_name, table_schema):
    return run_query("""CREATE TABLE {} ({});""".format(
        table_name,
        ", ".join("{} {}".format(name, type_) for name, type_ in table_schema)
    ))

def reset_table(table_name, table_schema):
    drop_table(table_name)
    create_table(table_name, table_schema)

def reset_all_tables():
    for s in DBConfig.schemas:
        table_name, table_schema = s.name, s.schema
        reset_table(table_name, table_schema)

