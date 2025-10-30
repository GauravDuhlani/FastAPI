from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


"""This is for connection to the SQLite3 database"""
SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})



"""This is for connecting to the Postgresql database"""
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234@localhost/TodoApplicationDatabase"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)



"""This is for connecting to the MySQL database"""
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234@127.0.0.1:3306/TodoApplicationDatabase"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
