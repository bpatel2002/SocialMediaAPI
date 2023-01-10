"""add content column to posts table

Revision ID: 92d667a5959a
Revises: bed1b2a05bdc
Create Date: 2023-01-09 20:46:38.107936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92d667a5959a'
down_revision = 'bed1b2a05bdc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
