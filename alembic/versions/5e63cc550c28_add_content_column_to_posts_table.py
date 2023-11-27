"""add content column to posts table

Revision ID: 5e63cc550c28
Revises: c9fb04dd4703
Create Date: 2023-11-26 13:38:33.762652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e63cc550c28'
down_revision: Union[str, None] = 'c9fb04dd4703'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
