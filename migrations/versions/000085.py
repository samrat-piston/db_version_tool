"""SQL migration with embedded SQL content

Revision ID: 000085
Revises: 000084
Create Date: 2026-05-26 14:07:42.453

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
import os

# revision identifiers, used by Alembic.
revision: str = '000085'
down_revision: Union[str, Sequence[str], None] = '000084'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade: Execute embedded SQL content"""

    # Execute upgrade SQL files directly:
    # From query_001.sql:
    with open("sql/000085/query_001.sql", "r") as f:
        sql_content_query_001 = f.read()
    op.execute(sa.text(sql_content_query_001))

    # From query_002.sql:
    with open("sql/000085/query_002.sql", "r") as f:
        sql_content_query_002 = f.read()
    op.execute(sa.text(sql_content_query_002))

    # From query_003.sql:
    with open("sql/000085/query_003.sql", "r") as f:
        sql_content_query_003 = f.read()
    op.execute(sa.text(sql_content_query_003))



def downgrade() -> None:
    """Downgrade: no rollback scripts bundled for this version."""
    pass
