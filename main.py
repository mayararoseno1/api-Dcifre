from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models
from . import crud 
from . import schemas
from . database import engine, SessionLocal # type: ignore

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

# Inicializar o FastAPI
app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar uma empresa
@app.post("/empresas/", response_model=schemas.Empresa)
def criar_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.criar_empresa(db=db, empresa=empresa)

# Rota para listar todas as empresas
@app.get("/empresas/", response_model=list[schemas.Empresa])
def listar_empresas(db: Session = Depends(get_db)):
    return crud.listar_empresas(db=db)

# Rota para criar uma obrigação acessória
@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoria)
def criar_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.criar_obrigacao(db=db, obrigacao=obrigacao)

# Rota para listar obrigações de uma empresa
@app.get("/empresas/{empresa_id}/obrigacoes/", response_model=list[schemas.ObrigacaoAcessoria])
def listar_obrigacoes(empresa_id: int, db: Session = Depends(get_db)):
    return crud.listar_obrigacoes_por_empresa(db=db, empresa_id=empresa_id)
