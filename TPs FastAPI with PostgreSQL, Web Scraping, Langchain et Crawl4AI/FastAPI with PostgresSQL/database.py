# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

USERNAME = "monuser"
PASSWORD = "monmôtrépassé"  # exemple avec accents
PASSWORD = quote_plus(PASSWORD)  # encode les caractères spéciaux
URL_DATABASE = f"postgresql://{USERNAME}:{PASSWORD}@localhost:5432/quizApp"

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()