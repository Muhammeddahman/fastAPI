"""add content table to posts table

Revision ID: c9fb04dd4703
Revises: cc4eb578bafe
Create Date: 2023-11-26 12:41:00.245340

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9fb04dd4703'
down_revision: Union[str, None] = 'cc4eb578bafe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
