import sqlalchemy as sa

from app.models.watchlist import Watchlist as db_watchlist
from app.schema.watchlist import WatchlistCreate, WatchlistUpdate

class Watchlist:
    def __init__(self, session) -> None:
        self.session = session

    def create_watchlist(self, user_id: int, watchlist: WatchlistCreate):
        watchlist = db_watchlist(
            movie_id=watchlist.movie_id,
            movie_title=watchlist.movie_title,
            note=watchlist.note,
            user_id=user_id
        )

        self.session.add(watchlist)
        self.session.commit()

        return watchlist

    def delete_watchlist(self, user_id: int, movie_id: int):
        watchlist_deleted = self.session.query(db_watchlist).filter(
            db_watchlist.user_id==user_id,
            db_watchlist.movie_id==movie_id
        ).delete(
            synchronize_session='fetch'
        )

        self.session.commit()

        return watchlist_deleted
    
    def update_watchlist(self, user_id: int, watchlist: WatchlistUpdate):
        watchlist_updated = self.session.query(db_watchlist).filter(
            db_watchlist.user_id==user_id,
            db_watchlist.movie_id==watchlist.movie_id
        ).update(
            {
                db_watchlist.note: watchlist.note
            },
            synchronize_session='fetch'
        )

        self.session.commit()

        return watchlist_updated

    def list_watchlist_per_user(self, user_id: int):
        users_watchlist = self.session.execute(
            sa.select(
                "*"
            ).where(
                db_watchlist.user_id==user_id
            )
        ).fetchall()

        return users_watchlist

    def list_watchlist(self):
        list_watchlist = self.session.query(db_watchlist).all()

        return list_watchlist
