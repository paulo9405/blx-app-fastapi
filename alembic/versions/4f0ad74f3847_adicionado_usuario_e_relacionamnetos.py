"""Adicionado Usuario e Relacionamnetos

Revision ID: 4f0ad74f3847
Revises: c993b6080efa
Create Date: 2021-06-06 23:52:06.582969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f0ad74f3847'
down_revision = 'c993b6080efa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.Column('telefone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_usuario_id'), ['id'], unique=False)

    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_usuario', 'usuario', ['usuario_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.drop_constraint('fk_usuario', type_='foreignkey')

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_usuario_id'))

    op.drop_table('usuario')
    # ### end Alembic commands ###
