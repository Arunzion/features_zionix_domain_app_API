"""create_initial_tables

Revision ID: 445cbc9b8b2b
Revises: 002
Create Date: 2025-05-27 06:54:00.535983
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '445cbc9b8b2b'
down_revision = '002'
branch_labels = None
depends_on = None

def upgrade():
    # Create domains table
    op.create_table(
        'domains',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('domain_name', sa.String(length=100), nullable=False),
        sa.Column('domain_code', sa.String(length=50), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('status', sa.Boolean(), nullable=True),
        sa.Column('action', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), onupdate=func.now()),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('domain_name'),
        sa.UniqueConstraint('domain_code')
    )

def downgrade():
    op.drop_table('domains')