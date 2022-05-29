from fastapi import Request
from sqlalchemy.orm import Session

from app.utils.db import db_engine
from app.utils.users import Users
from app.schema.users import UserCreate
from app.utils.json_response import JsonResponse


def create_user(request:Request, user_create_schema: UserCreate):
    redis = request.app.redis
    redis_key = f"user-list"
    with Session(db_engine) as session:
        user_class = Users(session=session)
        created_user = user_class.create_user(
            user_create_schema
        )

        data = {
            "id": created_user.id,
            "name": created_user.name
        }

        #invalidate user-list if new user created
        redis.invalidate(redis_key)

        return JsonResponse(data=data)



