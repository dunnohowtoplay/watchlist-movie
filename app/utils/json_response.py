import typing
from fastapi.responses import JSONResponse


def JsonResponse(data: typing.Any = None, message: str = 'Success', status_code: int = 200, code: int = None, success: bool = None):
    if success is None:
        success = status_code >= 200 and status_code < 300

    code = 1 if success else 0
    
    return JSONResponse(
        {
            'data': data,
            'message': message,
            'code': code,
            'success': success
        },
        status_code=status_code
    )
