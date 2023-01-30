"""create account color

Revision ID: 2291a317541a
Revises: 
Create Date: 2023-01-28 15:48:59.706579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2291a317541a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'Colour',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.Column('name', sa.String()),
        sa.Column('hex_code', sa.String()),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('Colour')
