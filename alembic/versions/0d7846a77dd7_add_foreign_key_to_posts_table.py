"""add foreign-key to posts table

Revision ID: 0d7846a77dd7
Revises: 50be44684a4a
Create Date: 2023-11-26 15:35:03.194652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d7846a77dd7'
down_revision: Union[str, None] = '50be44684a4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(), nullable=False))
    op.create_foreign_key(
        'posts_users_fk', source_table="posts", referent_table="users",local_cols=['owner_id'],remote_cols=['id'], ondelete="CASCADE")
    
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk',table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
