"""SQL migration with embedded SQL content

Revision ID: 000091
Revises: 000090
Create Date: 2026-07-13 17:37:10.563

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
import os

# revision identifiers, used by Alembic.
revision: str = '000091'
down_revision: Union[str, Sequence[str], None] = '000090'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade: Execute embedded SQL content"""

    # Execute upgrade SQL files directly:
    # From query_001.sql:
    with open("sql/000091/query_001.sql", "r") as f:
        sql_content_query_001 = f.read()
    op.execute(sa.text(sql_content_query_001))



def downgrade() -> None:
    """Downgrade: Execute embedded downgrade SQL content"""

    # Execute downgrade SQL files directly:
    # From downgrade.sql:
    with open("sql/000091/downgrade.sql", "r") as f:
        sql_content_downgrade = f.read()
    op.execute(sa.text(sql_content_downgrade))

