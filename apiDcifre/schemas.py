from pydantic import BaseModel, EmailStr
from typing import List, Optional


# Esquema para criação e retorno de Empresa
class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str


class EmpresaCreate(EmpresaBase):
    pass


class EmpresaResponse(EmpresaBase):
    id: int

    class Config:
        from_attributes = True


# Esquema para criação e retorno de ObrigacaoAcessoria
class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str  # Ex: "mensal", "trimestral", "anual"
    empresa_id: int


class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass


class ObrigacaoAcessoriaResponse(ObrigacaoAcessoriaBase):
    id: int

    class Config:
        from_attributes = True


# Para listar as obrigações de uma empresa
class EmpresaDetalhada(EmpresaResponse):
    obrigacoes: List[ObrigacaoAcessoriaResponse] = []
