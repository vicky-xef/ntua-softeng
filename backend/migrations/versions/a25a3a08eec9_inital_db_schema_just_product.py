"""Initial db schema, just product

Revision ID: a25a3a08eec9
Revises: 
Create Date: 2018-12-24 21:03:20.969570

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a25a3a08eec9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', mysql.MEDIUMTEXT(), nullable=True),
    sa.Column('category', sa.String(length=128), nullable=False),
    sa.Column('withdrawn', sa.Boolean(), nullable=False),
    sa.Column('tags', mysql.MEDIUMTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###