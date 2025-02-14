from sqlalchemy.orm import Session
from models import Empresa, ObrigacaoAcessoria
from schemas import EmpresaCreate, ObrigacaoAcessoriaCreate

# Função para criar uma empresa
def criar_empresa(db: Session, empresa: EmpresaCreate):
    nova_empresa = Empresa(
        nome=empresa.nome,
        cnpj=empresa.cnpj,
        endereco=empresa.endereco,
        email=empresa.email,
        telefone=empresa.telefone
    )
    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)
    return nova_empresa

# Função para obter uma empresa pelo ID
def obter_empresa(db: Session, empresa_id: int):
    return db.query(Empresa).filter(Empresa.id == empresa_id).first()

# Função para listar todas as empresas
def listar_empresas(db: Session):
    return db.query(Empresa).all()

# Função para criar uma obrigação acessória
def criar_obrigacao(db: Session, obrigacao: ObrigacaoAcessoriaCreate):
    nova_obrigacao = ObrigacaoAcessoria(
        nome=obrigacao.nome,
        periodicidade=obrigacao.periodicidade,
        empresa_id=obrigacao.empresa_id
    )
    db.add(nova_obrigacao)
    db.commit()
    db.refresh(nova_obrigacao)
    return nova_obrigacao

# Função para obter todas as obrigações de uma empresa
def listar_obrigacoes_por_empresa(db: Session, empresa_id: int):
    return db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.empresa_id == empresa_id).all()
