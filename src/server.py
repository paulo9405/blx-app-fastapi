from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm.session import Session
from src.schemas.schemas import Produto, Usuario, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario


#criar_db()

app = FastAPI()

# CORS
origins = [
    'http://localhost:3000',
    'https://myapp.vercel.com'
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PRODUTOS

@app.post('/produtos', status_code=status.HTTP_201_CREATED,
    response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos', response_model=List[Produto]) #response_model=List[ProdutoSimples]
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@app.get('/produtos/{produto_id}')
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).obter(produto_id)
    return produto


@app.delete('/produtos/{produto_id}')
def delete_produto(produto_id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(produto_id)
    return {'msg': 'Produto removido com sucesso'}


@app.put('/produtos/{produto_id}', response_model=ProdutoSimples)
def update_produto(produto_id: int, produto: Produto,
    db: Session = Depends(get_db)):
    RepositorioProduto(db).update(produto_id, produto)
    produto.id = produto_id
    return produto


#------------------------------------------------------------------------------------------------------
# USUARIOS

@app.post('/usuarios', status_code=status.HTTP_201_CREATED, 
    response_model=Usuario)
def criar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado
    

@app.get('/usuarios', response_model=List[Usuario])
def listar_usuario(db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).listar()
    return usuario

@app.get('/usuarios/{usuario_id}')
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).obter(usuario_id)
    return usuario


@app.delete('/usuarios/{usuario_id}')
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    RepositorioUsuario(db).remover(usuario_id)
    return {'msg': 'Removido com sucesso'}

@app.put('/usuarios/{usuario_id}')
def update_usuario(usuario_id: int, usuario: Usuario, 
    db: Session = Depends(get_db)):
    RepositorioUsuario(db).update(usuario_id, usuario)
    return {'msg': 'Usuario atualizado'}