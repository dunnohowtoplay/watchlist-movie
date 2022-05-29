from fastapi import Request
from sqlalchemy.orm import Session

from app.utils.db import db_engine
from app.utils.watchlist import Watchlist
from app.utils.json_response import JsonResponse


def list_watchlist(request:Request):
    redis_key = f"watchlist-list"
    redis = request.app.redis
    if redis.exists(redis_key):
        try:
            data = redis.get(redis_key)
            return JsonResponse(data=data)
        except:
            data = []

    with Session(db_engine) as session:
        watchlist_class = Watchlist(session=session)
        list_watchlist = watchlist_class.list_watchlist()
        
        data = []
        for watchlist in list_watchlist:
            data.append(
                {
                    "id":watchlist.id,
                    "movie_id":watchlist.movie_id,
                    "movie_title":watchlist.movie_title,
                    "note":watchlist.note,
                    "user_id":watchlist.user_id,
                    "created": watchlist.created.strftime('%Y-%m-%d %H:%M:%S') if watchlist.created and not isinstance(watchlist.created, str) else '',
                    "modified": watchlist.modified.strftime('%Y-%m-%d %H:%M:%S') if watchlist.modified and not isinstance(watchlist.modified, str) else '',
                }
            ) 

        redis.set(redis_key, data)

        return JsonResponse(data=data)



