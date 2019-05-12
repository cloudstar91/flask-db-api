"""empty message

Revision ID: ce103bf53031
Revises: f0723c3de79d
Create Date: 2019-05-11 17:11:08.349261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce103bf53031'
down_revision = 'f0723c3de79d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('types',
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name=op.f('fk_types_subject_id_subject')),
    sa.ForeignKeyConstraint(['type_id'], ['type.id'], name=op.f('fk_types_type_id_type')),
    sa.PrimaryKeyConstraint('type_id', 'subject_id', name=op.f('pk_types'))
    )
    op.create_table('locations',
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], name=op.f('fk_locations_location_id_location')),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name=op.f('fk_locations_subject_id_subject')),
    sa.PrimaryKeyConstraint('location_id', 'subject_id', name=op.f('pk_locations'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('locations')
    op.drop_table('types')
    # ### end Alembic commands ###
