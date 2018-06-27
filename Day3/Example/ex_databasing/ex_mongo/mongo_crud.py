# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import pymongo

# Create connection
conn = pymongo.MongoClient(host='localhost', port=27017)

# Select the database
# if it doesnt exist then it will be created
db_conn = conn.other_database

# Select the collection to insert into
# if it doesnt exist then it will be created
# after getting that collection we are dropping it so there wont be any existing values

col_conn = db_conn.my_collection
col_conn.drop()
col_conn = db_conn.my_collection



def crud():
    # Insert a document
    one_res = col_conn.insert_one({"name": "John", "salary": 100})
    print('One Inserted', one_res)
    # Insert many documents
    many_res = col_conn.insert_many([{ "name": "Jeorge", "salary": 100}, 
                          { "name": "Steve", "salary": 100},
                          { "name": "David", "salary": 100}]
                        )
    print('Many Inseretd', many_res)
    # Find one document
    print(col_conn.find_one())

    # Find all documents
    print('We can iterate through this cursor=>', col_conn.find())
    for result in col_conn.find():
        print('All results=>', result)

    # Find Where
    print('Find where result', col_conn.find_one({"name": "Steve"}))

    # Update ONE
    # Where name is John set name to Joseph
    col_conn.update_one({"name": "John"}, {"$set": {"name": "Joseph"}})
    print('After one update result')
    for result in col_conn.find():
        print('All results=>', result)

    # Update all (many)
    col_conn.update_many({"name": "John"}, {"$set": {"name": "Joseph"}})
    print('After many update result')
    for result in col_conn.find():
        print('All results=>', result)

    # Delete ONE
    col_conn.delete_one({"name": "Joseph"})
    print('After one delete result')
    for result in col_conn.find():
        print('All results=>', result)

    print('After many delete result')
    col_conn.delete_many({"salary": 100})
    for result in col_conn.find():
        print('All results=>', result)

def main():
    crud()


if __name__ == "__main__":
    main()
