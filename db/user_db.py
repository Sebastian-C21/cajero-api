from enum import unique
from typing import Dict
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine

class UserInDB(Base): #así se hace la herencia le python
    __tablename__ = "users"
    username = Column(String, primary_key=True, unique=True)
    password = Column(String)
    balance = Column(Integer)
Base.metadata.create_all(bind=engine)

"""
#definiendo la base de dato ficticia
database_users = Dict[str, UserInDB]

database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "balance":12000}),
    "andres18": UserInDB(**{"username":"andres18",
                            "password":"holaa",
                            "balance":78000})
}
"""

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db

def get_password(user: str, password: str):
    if user in database_users.keys():
        return print(database_users[user].username)
    else:
        return None
