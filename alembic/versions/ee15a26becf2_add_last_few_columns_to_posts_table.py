"""add last few columns to posts table

Revision ID: ee15a26becf2
Revises: 0d7846a77dd7
Create Date: 2023-11-26 19:29:08.527192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee15a26becf2'
down_revision: Union[str, None] = '0d7846a77dd7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('puplished',sa.Boolean(), nullable=False,server_default='True'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True), nullable=False,server_default=sa.text('NOW()')))
    pass

def downgrade() -> None:
    op.drop_column('posts', 'puplished')
    op.drop_column('posts', 'created_at')
    pass
