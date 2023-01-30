from fastapi import APIRouter
from fastapi_pagination import Page
from fastapi_pagination import paginate

from core import schemas
from core.database import db
from core.exception import DoesNotExistsException
from core.models import Colour
from core.schemas import ColorCreateUpdate

color_routes_v1 = APIRouter()


@color_routes_v1.get(
    '/',
    response_model=Page[schemas.ColorList],
    tags=['Color']
)
def get_list():
    return paginate(db.query(Colour).all())


@color_routes_v1.post(
    '/',
    response_model=schemas.ColorCreateUpdate,
    tags=['Color'],
    status_code=201
)
def create(data: ColorCreateUpdate):
    db_item = ColorCreateUpdate(**data.dict())
    instance = Colour(**db_item.dict())
    db.add(instance)
    db.commit()
    return db_item


@color_routes_v1.get(
    '/{color_id}',
    response_model=schemas.ColorList,
    tags=['Color'],
    status_code=200
)
def detail(color_id: int, data: ColorCreateUpdate):
    color = db.query(Colour).get(color_id)
    if color is None:
        raise DoesNotExistsException
    return color


@color_routes_v1.put(
    '/{color_id}',
    response_model=schemas.ColorList,
    tags=['Color'],
    status_code=200
)
def update(color_id: int, data: ColorCreateUpdate):
    color = db.query(Colour).get(color_id)
    if color is None:
        raise DoesNotExistsException
    for key, value in data:
        if key != 'id':
            setattr(color, key, value)
    db.commit()
    return color


@color_routes_v1.delete(
    '/{color_id}',
    tags=['Color'],
    status_code=204
)
def delete(color_id: int):
    color = db.query(Colour).filter(Colour.id == color_id)
    if color.count():
        color.delete()
        db.commit()
        return True
    raise DoesNotExistsException
