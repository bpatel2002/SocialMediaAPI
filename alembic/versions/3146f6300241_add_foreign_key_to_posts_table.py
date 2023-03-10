"""add foreign key to posts table

Revision ID: 3146f6300241
Revises: c8eed192bbcc
Create Date: 2023-01-09 20:54:53.536580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3146f6300241'
down_revision = 'c8eed192bbcc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",
                          referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
