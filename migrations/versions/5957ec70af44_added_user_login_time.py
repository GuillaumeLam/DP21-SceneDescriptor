"""Added user login time

Revision ID: 5957ec70af44
Revises: 8342714970ad
Create Date: 2019-06-27 00:39:48.486518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5957ec70af44'
down_revision = '8342714970ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('current_login_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'current_login_at')
    # ### end Alembic commands ###