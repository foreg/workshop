"""requests table

Revision ID: 070ea1a058d0
Revises: 43935e6cc695
Create Date: 2019-03-09 20:59:04.842212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '070ea1a058d0'
down_revision = '43935e6cc695'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('request_client_id_fkey', 'request', type_='foreignkey')
    op.drop_constraint('request_service_id_fkey', 'request', type_='foreignkey')
    op.create_foreign_key(None, 'request', 'service', ['service_id'], ['id'], ondelete='RESTRICT')
    op.create_foreign_key(None, 'request', 'client', ['client_id'], ['id'], ondelete='RESTRICT')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.create_foreign_key('request_service_id_fkey', 'request', 'service', ['service_id'], ['id'])
    op.create_foreign_key('request_client_id_fkey', 'request', 'client', ['client_id'], ['id'])
    # ### end Alembic commands ###
