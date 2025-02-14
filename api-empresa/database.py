from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

DATABASE_URL = os.getenv("psql postgresql://postgres:1234@localhost:5432/api_dcifre")

# Criar engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Criar sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Dependência para obter a sessão do banco em cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
