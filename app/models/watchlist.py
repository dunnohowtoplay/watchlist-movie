import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.models import Base
from app.models.users import Users

class Watchlist(Base):
    __tablename__ = "watchlist"

    id = sa.Column('id', sa.Integer, primary_key=True, index=True)
    movie_id = sa.Column('movie_id', sa.Integer, nullable=False)
    movie_title = sa.Column('movie_title', sa.String, index=True)
    note = sa.Column('note', sa.Text)
    user_id = sa.Column(sa.Integer, sa.ForeignKey(Users.id), nullable=False)
    created = sa.Column('created', sa.DateTime, server_default=sa.func.now())
    modified = sa.Column('modified', sa.DateTime, onupdate=sa.func.now())

    user = relationship("Users")
