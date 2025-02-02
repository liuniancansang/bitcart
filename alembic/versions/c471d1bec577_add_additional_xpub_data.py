"""Add additional xpub data

Revision ID: c471d1bec577
Revises: be1f56ed9798
Create Date: 2022-11-26 14:56:48.405282

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "c471d1bec577"
down_revision = "be1f56ed9798"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("wallets", sa.Column("additional_xpub_data", sa.JSON(), nullable=True, server_default="{}"))
    op.alter_column("wallets", "additional_xpub_data", server_default=None)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("wallets", "additional_xpub_data")
    # ### end Alembic commands ###
