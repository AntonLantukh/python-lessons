from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Status(BaseModel):
    value: bool


@router.post('/')
def set_status(status: Status):
    return {
        "data": {
            **status.model_dump(),
        }
    }


@router.get('/')
def get_status():
    return {
        "data": {
            "value": True
        }
    }
