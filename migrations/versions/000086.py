"""SQL migration with embedded SQL content

Revision ID: 000086
Revises: 000085
Create Date: 2026-05-26 15:59:49.102

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
import os

# revision identifiers, used by Alembic.
revision: str = '000086'
down_revision: Union[str, Sequence[str], None] = '000085'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade: Execute embedded SQL content"""

    # Execute upgrade SQL files directly:
    # From query_001.sql:
    with open("sql/000086/query_001.sql", "r") as f:
        sql_content_query_001 = f.read()
    op.execute(sa.text(sql_content_query_001))

    # From query_002.sql:
    with open("sql/000086/query_002.sql", "r") as f:
        sql_content_query_002 = f.read()
    op.execute(sa.text(sql_content_query_002))



def downgrade() -> None:
    """Downgrade: no rollback scripts bundled for this version."""
    pass
