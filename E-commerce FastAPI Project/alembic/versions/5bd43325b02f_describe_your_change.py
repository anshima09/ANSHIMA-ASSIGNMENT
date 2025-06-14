"""Describe your change

Revision ID: 5bd43325b02f
Revises: 84cd25008353
Create Date: 2025-06-15 13:51:15.445960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bd43325b02f'
down_revision: Union[str, None] = '84cd25008353'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'is_deleted')
    # ### end Alembic commands ###
