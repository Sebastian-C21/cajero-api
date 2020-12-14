from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy import Column, ForeignKey,
from sqlalchemy import Integer, String, DateTime
import datetime
from db.db_connection import Base, engine

class TransactionInDB(Base):
    __tablename__ = "transactions"
    id_transaction = Column(Integer,primary_key=True,autoincerement=True)
    username = Column(String)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    value = Column(Integer)
    actual_balance = Column(Integer)
Base.metadata.create_all(bind=engine)

"""
database_transactions = []
generator = {"id": 0}


def save_transaction(transaction_in_db: TransactionInDB):
    generator["id"] = generator["id"] + 1
    transaction_in_db.id_transaction = generator["id"]
    database_transactions.append(transaction_in_db)
    return transaction_in_db
"""