import json
from typing import Any, Dict, Optional

from fastapi import HTTPException
from starlette.responses import JSONResponse


def custom_validation_exception_handler(exc):
    exc_json = json.loads(exc.json())
    response = {'error': []}
    for error in exc_json:
        response['error'].append({error['loc'][-1]: error['msg']})

    return JSONResponse(response, status_code=400)


class DoesNotExistsException(HTTPException):

    def __init__(self, status_code: int = 404, detail: Any = 'Record Not Found', headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)
