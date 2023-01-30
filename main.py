from fastapi import FastAPI
from core import models
from core.database import engine
from core.api.color.color import color_routes_v1
from fastapi_pagination import add_pagination
from fastapi.exceptions import RequestValidationError
from fastapi.exceptions import ValidationError
from core.exception import custom_validation_exception_handler

tags_metadata = [
    {
        'name': 'Color',
    }
]

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Crud', openapi_tags=tags_metadata)
app.include_router(color_routes_v1, prefix='/v1/color')

add_pagination(app)


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
def validation(request, exc):
    return custom_validation_exception_handler(exc)
