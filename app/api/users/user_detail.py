from fastapi import Request
from sqlalchemy.orm import Session

from app.utils.db import db_engine
from app.utils.users import Users
from app.utils.json_response import JsonResponse


def detail_user(request: Request, user_id: int):
    redis_key = f"user-detail:{user_id}"
    redis = request.app.redis
    if redis.exists(redis_key):
        try:
            data = redis.get(redis_key)
            return JsonResponse(data=data)
        except:
            data = []

    with Session(db_engine) as session:
        user_class = Users(session=session)
        detail_user = user_class.detail_user(
           user_id=user_id
        )

        if not detail_user:
            return JsonResponse(message=f"User not found", status_code=404)
        
        data = {
            "id": detail_user.id,
            "name": detail_user.name,
            "created": detail_user.created.strftime('%Y-%m-%d %H:%M:%S') if detail_user.created and not isinstance(detail_user.created, str) else '',
            "modified": detail_user.modified.strftime('%Y-%m-%d %H:%M:%S') if detail_user.modified and not isinstance(detail_user.modified, str) else '',
        }
        # only set to redis if data exists
        redis.set(redis_key, data)

        return JsonResponse(data=data)



