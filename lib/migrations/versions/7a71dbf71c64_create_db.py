"""create db

Revision ID: 7a71dbf71c64
Revises: 
Create Date: 2023-03-15 15:05:55.516631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a71dbf71c64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('founding_year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('companies')