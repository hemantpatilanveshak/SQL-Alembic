"""create game table

Revision ID: f06c62dcb58b
Revises: 
Create Date: 2024-02-02 14:18:28.716283

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f06c62dcb58b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "game",
        sa.Column("id",sa.Integer,primary_key = True),
        sa.Column("name",sa.String(50),nullable = False),
        sa.Column("year_of_release",sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table("game")
