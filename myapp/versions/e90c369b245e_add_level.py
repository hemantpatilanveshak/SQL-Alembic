"""add level

Revision ID: e90c369b245e
Revises: f06c62dcb58b
Create Date: 2024-02-02 14:27:32.512676

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e90c369b245e'
down_revision: Union[str, None] = 'f06c62dcb58b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "game",
        sa.Column('level',sa.Integer,nullable = True)
    )


def downgrade() -> None:
    op.drop_column('game','level')
