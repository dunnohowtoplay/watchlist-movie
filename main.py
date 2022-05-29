import uvicorn

from app.config import settings

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='0.0.0.0',
        port=settings.PORT,
        debug=settings.DEBUG,
        log_level=settings.DEBUG
    )