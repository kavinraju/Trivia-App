"""empty message

Revision ID: b2ca44b8bb51
Revises: 2c0d4bb1b2cb
Create Date: 2020-05-08 07:30:27.573588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2ca44b8bb51'
down_revision = '2c0d4bb1b2cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('questions', 'category',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('questions', 'category',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
