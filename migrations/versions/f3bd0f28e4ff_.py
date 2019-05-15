"""empty message

Revision ID: f3bd0f28e4ff
Revises: f99bc922bab0
Create Date: 2019-05-15 22:31:01.790222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3bd0f28e4ff'
down_revision = 'f99bc922bab0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subjectlocation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subjectlocation',
    sa.Column('subject_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('location_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], name='fk_subjectlocation_location_id_location'),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name='fk_subjectlocation_subject_id_subject')
    )
    # ### end Alembic commands ###