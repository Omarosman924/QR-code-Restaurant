from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# الاتصال بقاعدة البيانات (PostgreSQL)
engine = create_engine("postgresql://user:pass@localhost:5432/mydb")
Base = declarative_base()
Session = sessionmaker(bind=engine)


