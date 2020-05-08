"""empty message

Revision ID: c1b889c3fef2
Revises: 462f4eb15f20
Create Date: 2020-05-08 07:19:20.197614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1b889c3fef2'
down_revision = '462f4eb15f20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('questions_category_fkey', 'questions', type_='foreignkey')
    op.create_foreign_key(None, 'questions', 'categories', ['category'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.create_foreign_key('questions_category_fkey', 'questions', 'categories', ['category'], ['id'])
    # ### end Alembic commands ###
