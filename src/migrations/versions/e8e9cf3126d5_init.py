"""init

Revision ID: e8e9cf3126d5
Revises: 
Create Date: 2024-06-28 17:34:29.870234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8e9cf3126d5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('web_page_source_code',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True, comment='Дата/время добавления в БД'),
    sa.Column('url', sa.String(length=300), nullable=False, comment='URL исходной кода'),
    sa.Column('source_code', sa.Text(), nullable=False, comment='Исходный код'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_web_page_source_code_id'), 'web_page_source_code', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_web_page_source_code_id'), table_name='web_page_source_code')
    op.drop_table('web_page_source_code')
    # ### end Alembic commands ###