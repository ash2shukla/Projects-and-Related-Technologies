# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
from os import getcwd, path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import MyMapping, Base

# Create system independent path to testdb sqlite db
# if db exists already then it will connect to that else it will create sqlite db itself
db_path = 'sqlite:///' + path.join(getcwd(), 'testdb')
print(db_path)
# connect to database echo=True will show all SQL queries that
# this engine will create and run
engine = create_engine(db_path, echo=True)


# Usually there exist some Tables in Relational Database
# and we map a class to that database
# But in sqlalchemy and almost all modern ORMs we can use declarative typing
# ie. we can delcare a table using a class (called Model) and it will create
# the table itself
Base.metadata.create_all(engine)

# Create a session class to the engine ie. to the database
Session = sessionmaker(bind=engine)
# Get a session
session = Session()


def crud():
    # Create an object of mapping
    # mymapping_object = MyMapping(name='ed', fullname='Ed Jones', password='edspassword')
    # # see what the object of mapping contains
    # print('\nThe mapping object is=>')
    # print(mymapping_object)
    # # add the object of mapping to the session to commit later
    # session.add(mymapping_object)
    # # Adding a lot of objects (rows) to the session to commit later
    # session.add_all([
    #         MyMapping(name='ed1', fullname='Ed Jones1', password='edspassword1'),
    #         MyMapping(name='ed2', fullname='Ed Jones2', password='edspassword2')
    #     ])
    # # see what is pending to be committed
    # print('\nPending to be commited after addition in session=>')
    # print(session.new)
    # # want to update something?
    # # just modify the corresponding attribute of that object
    # mymapping_object.name = 'eddy'
    # print('\nPending to be commited after changes in session=>')
    # print(session.new)
    # # Commit the queries to the database
    # session.commit()
    # Reading from data base
    # query the database that if the name attribute is any of the strings from ed, ed1 or ed2
    results = session.query(MyMapping).filter(MyMapping.name.in_(['ed', 'ed1', 'ed2']))
    # print all of the results
    # we can see that session is acting quite like our cursor in usual RDBs
    all_results = results.all()
    print('\nThe retrieved results=>')
    print(all_results)


def main():
    crud()
    # pass


if __name__ == "__main__":
    main()
