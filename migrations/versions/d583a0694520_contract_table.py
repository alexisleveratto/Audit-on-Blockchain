"""contract table

Revision ID: d583a0694520
Revises: f84f3343fd86
Create Date: 2020-03-21 18:48:36.301849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd583a0694520'
down_revision = 'f84f3343fd86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contract', sa.Column('client_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contract', 'user', ['client_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contract', type_='foreignkey')
    op.drop_column('contract', 'client_id')
    # ### end Alembic commands ###