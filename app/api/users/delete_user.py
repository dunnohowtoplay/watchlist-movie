from fastapi import Request
from sqlalchemy.orm import Session

from app.utils.db import db_engine
from app.utils.users import Users
from app.utils.json_response import JsonResponse


def delete_user(request:Request, user_id: int):
    redis = request.app.redis
    redis_key_user_list = f"user-list"
    redis_key_user_detail = f"user-detail:{user_id}"

    with Session(db_engine) as session:
        user_class = Users(session=session)
        deleted_user = user_class.delete_user(
           user_id=user_id
        )

        if not deleted_user:
            return JsonResponse(message=f"User not found", status_code=404)

        #invalidate user-list, detail if deleted
        redis.invalidate(redis_key_user_list)
        redis.invalidate(redis_key_user_detail)
        return JsonResponse(message=f"Success delete user {deleted_user}")



