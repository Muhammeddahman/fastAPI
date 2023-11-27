"""create posts table

Revision ID: cc4eb578bafe
Revises: 
Create Date: 2023-11-26 00:04:22.388387

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc4eb578bafe'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts", sa.Column('id',sa.Integer(), primary_key=True, nullable=False), sa.Column('title',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.create_table("posts")
    pass
