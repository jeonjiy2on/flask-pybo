"""empty message

Revision ID: 22afed2629ce
Revises: b0ac9aef487c
Create Date: 2021-04-22 14:29:18.366497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22afed2629ce'
down_revision = 'b0ac9aef487c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
