"""Describe your change

Revision ID: 38961ae03fa4
Revises: 0d80b0761880
Create Date: 2025-06-15 11:52:03.551631

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38961ae03fa4'
down_revision: Union[str, None] = '0d80b0761880'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order_items', 'product_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('products', 'is_deleted')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('is_deleted', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False))
    op.alter_column('order_items', 'product_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
