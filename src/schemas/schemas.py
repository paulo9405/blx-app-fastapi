# os Schemas são os dados que vão chegar para o usuario.
from pydantic import BaseModel
from typing import Optional, List

from sqlalchemy.sql.expression import true


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    disponivel: bool
    

    class Config:
        orm_mode = True


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimples]  =[]
    class Config:       #quando vem do banco de dados os atributos não ficam numa forma dicionario, eles ficam na forma de objetos, tem que usar o ponto(.) para cada um dos atributos
        orm_mode = True 


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:       
        orm_mode = True 
    

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int] 
    usuario: Optional[UsuarioSimples] # tem que colocar como opcional pq se nao vai reclamar que tem q colocar como objeto usuario

    class Config:
        orm_mode = True 
 

class Pedido(BaseModel):
    id: Optional[str] = None
    
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações' 