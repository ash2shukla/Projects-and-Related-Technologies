# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class MyMapping(Base):
    __tablename__ = 'mymapping'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
       string = f"<MyMapping(name={self.name}, fullname={self.fullname}, password={self.password})>"
       return string


def main():
    pass

if __name__ == "__main__":
    main()
