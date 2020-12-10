from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel): #así se hace la herencia le python
    username: str
    password: str
    balance: int

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
