"""empty message

Revision ID: 24be1321785d
Revises: 099539ca7da1
Create Date: 2018-08-30 15:15:38.286823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24be1321785d'
down_revision = '099539ca7da1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('u_token', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'u_token')
    # ### end Alembic commands ###