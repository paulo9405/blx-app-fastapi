from fastapi import APIRouter, Depends, status
from typing import List
from src.schemas.schemas import Usuario
from sqlalchemy.orm.session import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario \
    import RepositorioUsuario

router = APIRouter()


@router.post('/usuarios', status_code=status.HTTP_201_CREATED, 
    response_model=Usuario)
def criar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado
    

@router.get('/usuarios', response_model=List[Usuario])
def listar_usuario(db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).listar()
    return usuario

@router.get('/usuarios/{usuario_id}')
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).obter(usuario_id)
    return usuario


@router.delete('/usuarios/{usuario_id}')
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    RepositorioUsuario(db).remover(usuario_id)
    return {'msg': 'Removido com sucesso'}

@router.put('/usuarios/{usuario_id}')
def update_usuario(usuario_id: int, usuario: Usuario, 
    db: Session = Depends(get_db)):
    RepositorioUsuario(db).update(usuario_id, usuario)
    return {'msg': 'Usuario atualizado'}
