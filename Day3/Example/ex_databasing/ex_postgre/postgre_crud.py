# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import psycopg2

# Create a connection to Database
conn = psycopg2.connect(dbname="testdb", user="dbuser", password="password", host="localhost", port=5432)

# Open a connection to Database
cur = conn.cursor()


def execute_and_commit(*SQLargs):
    cur.execute(*SQLargs)
    conn.commit()


def crud():
    try:
        # Create a table
        execute_and_commit("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    except psycopg2.ProgrammingError:
        # If a fault occurs then we must rollback that transaction
        conn.rollback()

    # Insert a record into table CREATE
    execute_and_commit("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

    # Read the inserted record from table
    cur.execute("SELECT * FROM test;")

    # Read one record out of the returned results
    print('>> Inserted Record', cur.fetchone())

    # Update a record
    execute_and_commit("UPDATE test SET num=%s WHERE data=%s", (200, "abc'def"))

    # Read the inserted record from table
    cur.execute("SELECT * FROM test;")

    # Read one record out of the returned results
    print('>> Updated Record', cur.fetchone())

    # Delete a record
    execute_and_commit("DELETE FROM test WHERE data=%s", ("abc'def", ))

    # Read the inserted record from table
    cur.execute("SELECT * FROM test;")

    # Read one record out of the returned results
    print('>> Record Deleted', cur.fetchone())


def main():
    crud()
    cur.close()
    conn.close()
    pass


if __name__ == "__main__":
    main()
