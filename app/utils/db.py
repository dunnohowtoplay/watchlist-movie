import sqlalchemy as sa
from app.config import settings

db_engine = sa.create_engine(
    settings.DB,
    pool_pre_ping=settings.DB_POOL_PRE_PING,
    pool_size=settings.DB_POOL_SIZE,
    pool_recycle=settings.DB_POOL_RECYCLE,
    echo=settings.DB_ECHO
)