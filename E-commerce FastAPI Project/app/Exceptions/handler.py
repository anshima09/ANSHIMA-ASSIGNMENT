
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import HTTPException, Request
from starlette.status import HTTP_400_BAD_REQUEST


def custom_http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Custom exception handler to return errors in a consistent JSON format.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "message": exc.detail,
            "code": exc.status_code
        },
    )


def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        loc = error.get("loc", [])
        msg = error.get("msg", "Invalid input.")
        
        # ✅ Specific case for email
        if "email" in loc:
            return JSONResponse(
                status_code=HTTP_400_BAD_REQUEST,
                content={
                    "error": True,
                    "message": "Invalid email format.",
                    "code": HTTP_400_BAD_REQUEST,
                },
            )
