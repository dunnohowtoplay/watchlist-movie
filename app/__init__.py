import typing
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError

from app.api import router
from app.utils.logger import logger
from app.utils.json_response import JsonResponse
from app.utils.redis_adapter import RedisAdapter
from app.config import settings

app_kwargs = dict(
    docs_url=f'/watchlist/docs',
    redoc_url=f'/watchlist/redoc',
    openapi_url=f'/watchlist/openapi.json',
    title="Watchlist API", 
    version="v1"
)

app = FastAPI(**app_kwargs)

app.redis = RedisAdapter(
    dict(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD
    ),
    prefix=settings.REDIS_PREFIX
)

@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, exc: HTTPException):
    message: str = exc.detail
    code: int = exc.status_code
    status_code: int = code

    return JsonResponse(
        message=message,
        code=code,
        status_code=status_code
    )

@app.exception_handler(Exception)
async def handle_unhandled_exception(request: Request, exc: Exception):
    logger.exception(exc)

    return JsonResponse(
        message='An error occured',
        code=500,
        status_code=500
    )


@app.exception_handler(RequestValidationError)
async def handle_validation_error(request: Request, exc: RequestValidationError):
    error_list: typing.List[dict] = exc.errors()
    error_messages: dict = {}
    for error in error_list:
        if len(error['loc']) < 2:
            return JsonResponse(data=error_messages, message='Please check your data', status_code=400, success=False)
        error_messages.update(
            {error['loc'][1]: error['msg']}
        )

    return JsonResponse(data=error_messages, message='Please check your data', status_code=400, success=False)


app.include_router(router)

