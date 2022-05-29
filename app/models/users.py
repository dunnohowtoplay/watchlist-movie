import sqlalchemy as sa

from app.models import Base

class Users(Base):
    __tablename__ = "users"

    id = sa.Column('id', sa.Integer, primary_key=True, index=True)
    name = sa.Column('name', sa.String(30), index=True, nullable=False)
    created = sa.Column('created', sa.DateTime, server_default=sa.func.now())
    modified = sa.Column('modified', sa.DateTime, onupdate=sa.func.now())

