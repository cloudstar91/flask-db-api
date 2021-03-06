"""empty message

Revision ID: f99bc922bab0
Revises: 44194fb1a53f
Create Date: 2019-05-15 14:56:51.578636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f99bc922bab0'
down_revision = '44194fb1a53f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###
