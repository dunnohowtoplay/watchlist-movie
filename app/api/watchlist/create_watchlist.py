from fastapi import Request
from sqlalchemy.orm import Session

from app.utils.db import db_engine
from app.utils.watchlist import Watchlist
from app.schema.watchlist import WatchlistCreate
from app.utils.json_response import JsonResponse


def create_watchlist(request:Request, user_id:int, watchlist:WatchlistCreate):
    redis_key_per_user = f"watchlist-list-per-user:{user_id}"
    redis_key = f"watchlist-list"
    redis = request.app.redis
    
    with Session(db_engine) as session:
        watchlist_class = Watchlist(session=session)
        watchlist = watchlist_class.create_watchlist(user_id=user_id, watchlist=watchlist)
        
        data = {
            "id":watchlist.id,
            "movie_id":watchlist.movie_id,
            "movie_title":watchlist.movie_title,
            "note":watchlist.note,
            "user_id":watchlist.user_id,
            "created": watchlist.created.strftime('%Y-%m-%d %H:%M:%S') if watchlist.created and not isinstance(watchlist.created, str) else '',
            "modified": watchlist.modified.strftime('%Y-%m-%d %H:%M:%S') if watchlist.modified and not isinstance(watchlist.modified, str) else '',
        }
        
        # invalidate if new watchlist created
        redis.invalidate(redis_key_per_user)
        redis.invalidate(redis_key)

        return JsonResponse(data=data)



