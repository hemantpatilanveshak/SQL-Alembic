"""591bd43c7e16 and ac3f94d7b0d6

Revision ID: b8fd049e22fb
Revises: 591bd43c7e16, ac3f94d7b0d6
Create Date: 2024-02-02 15:20:56.313833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8fd049e22fb'
down_revision: Union[str, None] = ('591bd43c7e16', 'ac3f94d7b0d6')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
