"""auto-vote

Revision ID: 909f1047e05f
Revises: ee15a26becf2
Create Date: 2023-11-26 19:57:00.265697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '909f1047e05f'
down_revision: Union[str, None] = 'ee15a26becf2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=True))
    op.drop_column('posts', 'puplished')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('puplished', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False))
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'content')
    # ### end Alembic commands ###
