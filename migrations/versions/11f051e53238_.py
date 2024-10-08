"""empty message

Revision ID: 11f051e53238
Revises: 579f6aa32774
Create Date: 2024-07-13 00:16:33.120221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11f051e53238'
down_revision = '579f6aa32774'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_stock_selections',
    sa.Column('login_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('stock_symbol', sa.String(length=100), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_name'], ['user.user_name'], ),
    sa.PrimaryKeyConstraint('login_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_stock_selections')
    # ### end Alembic commands ###
