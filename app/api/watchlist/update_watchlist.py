from fastapi import Request
from sqlalchemy.orm import Session

from app.utils.db import db_engine
from app.utils.watchlist import Watchlist
from app.schema.watchlist import WatchlistUpdate
from app.utils.json_response import JsonResponse


def update_watchlist(request:Request, user_id:int, watchlist:WatchlistUpdate):
    redis_key_per_user = f"watchlist-list-per-user:{user_id}"
    redis_key = f"watchlist-list"
    redis = request.app.redis

    with Session(db_engine) as session:
        watchlist_class = Watchlist(session=session)
        updated_watchlist = watchlist_class.update_watchlist(user_id=user_id, watchlist=watchlist)
        
        if not updated_watchlist:
            return JsonResponse(message=f"Watchlist not found", status_code=404)

        # invalidate if watchlist deleted
        redis.invalidate(redis_key_per_user)
        redis.invalidate(redis_key)
        
        return JsonResponse(message=f"Success Update Watchlist {updated_watchlist}")



