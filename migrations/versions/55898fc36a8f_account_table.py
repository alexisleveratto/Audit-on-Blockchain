"""account table

Revision ID: 55898fc36a8f
Revises: 8ed6c6f92eaa
Create Date: 2020-03-22 13:23:53.176989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "55898fc36a8f"
down_revision = "8ed6c6f92eaa"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "account",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name_account", sa.String(length=128), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_account_name_account"), "account", ["name_account"], unique=False
    )
    op.drop_index("ix_accounts_name_account", table_name="accounts")
    op.drop_table("accounts")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "accounts",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("name_account", sa.VARCHAR(length=128), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_accounts_name_account", "accounts", ["name_account"], unique=False
    )
    op.drop_index(op.f("ix_account_name_account"), table_name="account")
    op.drop_table("account")
    # ### end Alembic commands ###
