from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
from sqlalchemy.sql.functions import mode
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():
    
    def __init__(self, db: Session):
        self.db = db

    
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel,
            usuario_id=produto.usuario_id
            )

        self.db .add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

#def listar(self):
#    produtos = self.db.query(models.Produto).all()
#    return produtos

    def listar(self):
        stmt = select(models.Produto)
        produtos = self.db.execute(stmt).scalars().all()
        return produtos


    def obter(self, produto_id: int):
        stmt = select(models.Produto).filter_by(id=produto_id)
        produto = self.db.execute(stmt).one()
        return produto


    def remover(self, produto_id: int):
        stmt = delete(models.Produto).where(models.Produto.id == produto_id)
        self.db.execute(stmt)
        self.db.commit()  
    

    def update(self, produto_id: int, produto: schemas.Produto):
        update_stmt = (
            update(models.Produto).where(models.Produto.id == produto_id).
            values(
                nome=produto.nome,
                detalhes=produto.detalhes,
                preco=produto.preco,
                disponivel=produto.disponivel,
                )
            )
        self.db.execute(update_stmt)
        self.db.commit()
       


