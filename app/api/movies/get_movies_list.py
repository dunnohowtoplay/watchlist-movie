from fastapi import Request

from app.utils.json_response import JsonResponse
from app.utils.get_movies import GetMovies

def get_movies_list(request: Request, page: int = 1):
    redis_key = f"movie-list:page-{page}"
    redis = request.app.redis
    if redis.exists(redis_key):
        try:
            data = redis.get(redis_key)
            return JsonResponse(data=data)
        except:
            data = []

    movie_class = GetMovies()
    data = movie_class.get_movie_list(page)
    # only set to redis if data exists
    if data:
        redis.set(redis_key, data)

    return JsonResponse(data=data)