"""empty message

Revision ID: c57d39899d06
Revises: ebeefd869c99
Create Date: 2019-05-12 12:46:22.318206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c57d39899d06'
down_revision = 'ebeefd869c99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tutor', sa.Column('subject_id', sa.Integer(), nullable=False))
    op.create_foreign_key(op.f('fk_tutor_subject_id_subject'), 'tutor', 'subject', ['subject_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_tutor_subject_id_subject'), 'tutor', type_='foreignkey')
    op.drop_column('tutor', 'subject_id')
    # ### end Alembic commands ###
