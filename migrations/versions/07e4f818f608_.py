"""empty message

Revision ID: 07e4f818f608
Revises: f3bd0f28e4ff
Create Date: 2019-05-16 00:09:37.836484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07e4f818f608'
down_revision = 'f3bd0f28e4ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subjectlocation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], name=op.f('fk_subjectlocation_location_id_location')),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name=op.f('fk_subjectlocation_subject_id_subject')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_subjectlocation'))
    )
    op.create_table('tutorlocation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tutor_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], name=op.f('fk_tutorlocation_location_id_location')),
    sa.ForeignKeyConstraint(['tutor_id'], ['tutor.id'], name=op.f('fk_tutorlocation_tutor_id_tutor')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tutorlocation'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tutorlocation')
    op.drop_table('subjectlocation')
    # ### end Alembic commands ###
