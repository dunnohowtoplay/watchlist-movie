from fastapi import Request
from sqlalchemy.orm import Session

from app.utils.db import db_engine
from app.utils.users import Users
from app.utils.json_response import JsonResponse


def list_users(request:Request):
    redis_key = f"user-list"
    redis = request.app.redis
    if redis.exists(redis_key):
        try:
            data = redis.get(redis_key)
            return JsonResponse(data=data)
        except:
            data = []

    with Session(db_engine) as session:
        user_class = Users(session=session)
        list_users = user_class.list_user()
        
        data = []
        for user in list_users:
            data.append(
                {
                    "id": user.id,
                    "name": user.name
                }
            ) 
        
        # only set to redis if data exists
        if data:
            redis.set(redis_key, data)

        return JsonResponse(data=data)



