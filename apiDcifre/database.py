from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Verificar se o arquivo .env está no diretório
env_path = os.path.join(os.path.dirname(__file__), '.env')
if not os.path.exists(env_path):
    print(f"Arquivo .env não encontrado no diretório: {env_path}")
else:
    print(f"Arquivo .env encontrado no diretório: {env_path}")

# Carregar variáveis do arquivo .env
load_dotenv(dotenv_path=env_path)

# Verificar se as variáveis de ambiente foram carregadas
for key, value in os.environ.items():
    if key.startswith("DATABASE"):
        print(f"{key}={value}")

# Obter a URL do banco de dados do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Adicionar print para depuração
print(f"DATABASE_URL: {DATABASE_URL}")

# Verificação para garantir que a URL foi carregada corretamente
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL não está definida no arquivo .env")

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