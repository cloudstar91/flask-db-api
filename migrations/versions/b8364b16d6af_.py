"""empty message

Revision ID: b8364b16d6af
Revises: c57d39899d06
Create Date: 2019-05-14 00:58:06.007732

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b8364b16d6af'
down_revision = 'c57d39899d06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tutor', sa.Column('hourlyrate', sa.Integer(), nullable=False))
    op.drop_column('tutor', 'rating')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tutor', sa.Column('rating', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.drop_column('tutor', 'hourlyrate')
    # ### end Alembic commands ###
