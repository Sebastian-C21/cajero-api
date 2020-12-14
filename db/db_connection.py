from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creando motor y conexión a la base de datos
DATABASE_URL = "postgresql://postgres:postgres981211@host:5432/MISIONTIC"
engine = create_engine(DATABASE_URL)

#creando sesión 
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Creando base para lacreación de los modelos
Base = declarative_base()
Base.metadata.schema = "cajerodb"