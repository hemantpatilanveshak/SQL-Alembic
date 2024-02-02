"""add field players

Revision ID: ac3f94d7b0d6
Revises: e90c369b245e
Create Date: 2024-02-02 15:11:57.838705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac3f94d7b0d6'
down_revision: Union[str, None] = 'e90c369b245e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "game",
        sa.Column('players',sa.Integer,nullable = True)
    )


def downgrade() -> None:
    op.drop_column('game','players')
