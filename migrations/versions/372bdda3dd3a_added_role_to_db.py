"""Added Role to db

Revision ID: 372bdda3dd3a
Revises: 60c6d9d09c93
Create Date: 2019-06-27 01:08:11.682523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '372bdda3dd3a'
down_revision = '60c6d9d09c93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role')
    # ### end Alembic commands ###
