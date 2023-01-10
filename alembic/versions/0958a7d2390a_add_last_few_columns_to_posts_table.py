"""add last few columns to posts table

Revision ID: 0958a7d2390a
Revises: 3146f6300241
Create Date: 2023-01-09 20:58:08.430135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0958a7d2390a'
down_revision = '3146f6300241'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
