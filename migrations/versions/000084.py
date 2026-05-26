"""SQL migration with embedded SQL content

Revision ID: 000084
Revises: '000083'
Create Date: 2026-05-25 12:47:05.473633

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
import os

# revision identifiers, used by Alembic.
revision: str = '000084'
down_revision: Union[str, Sequence[str], None] = '000083'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade: Execute embedded SQL content"""

    # Execute upgrade SQL files directly:
    # From upgrade.sql:
    with open("sql/000084/upgrade.sql", "r") as f:
        sql_content_upgrade_sql = f.read()
    op.execute(sa.text(sql_content_upgrade_sql))




def downgrade() -> None:
    """Downgrade: Execute embedded downgrade SQL content"""

    # Execute downgrade SQL files directly:
    # From downgrade.sql:
    with open("sql/000084/downgrade.sql", "r") as f:
        sql_content_downgrade_sql = f.read()
    op.execute(sa.text(sql_content_downgrade_sql))