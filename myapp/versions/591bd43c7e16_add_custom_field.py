"""add custom field

Revision ID: 591bd43c7e16
Revises: e90c369b245e
Create Date: 2024-02-02 15:14:16.939641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '591bd43c7e16'
down_revision: Union[str, None] = 'e90c369b245e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "game",
        sa.Column('custom',sa.String(50),nullable = True)
    )


def downgrade() -> None:
    op.drop_column('game','custom')
