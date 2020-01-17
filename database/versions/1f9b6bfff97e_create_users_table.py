"""create users table

Revision ID: 1f9b6bfff97e
Revises: 36d29f362525
Create Date: 2019-10-15 16:15:58.827570

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as su

# revision identifiers, used by Alembic.
revision = '1f9b6bfff97e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('username', sa.VARCHAR(length=100), nullable=False),
        sa.Column('password', sa.CHAR(length=41), nullable=False),
        sa.Column('name', sa.VARCHAR(length=30), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        mysql_charset='utf8mb4',
        mysql_collate='utf8mb4_unicode_ci',
        mysql_engine='InnoDB',
        mysql_row_format='DYNAMIC'
    )
    pass


def downgrade():
    op.drop_table('Users')
    pass
