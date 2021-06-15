from fastapi import APIRouter, Depends, status
from typing import List
from src.schemas.schemas import Produto, ProdutoSimples
from sqlalchemy.orm.session import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_produto \
    import RepositorioProduto


router = APIRouter()

@router.post('/produtos', status_code=status.HTTP_201_CREATED,
    response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@router.get('/produtos', response_model=List[Produto]) #response_model=List[ProdutoSimples]
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@router.get('/produtos/{produto_id}')
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).obter(produto_id)
    return produto


@router.delete('/produtos/{produto_id}')
def delete_produto(produto_id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(produto_id)
    return {'msg': 'Produto removido com sucesso'}


@router.put('/produtos/{produto_id}', response_model=ProdutoSimples)
def update_produto(produto_id: int, produto: Produto,
    db: Session = Depends(get_db)):
    RepositorioProduto(db).update(produto_id, produto)
    produto.id = produto_id
    return produto