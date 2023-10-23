from typing import Annotated, Generic, TypeVar
from fastapi import APIRouter, status, Path
from pydantic import BaseModel

router = APIRouter()

DataT = TypeVar('DataT')


class BaseUser(BaseModel):
    name: str
    surname: str
    age: int
    address: str


class User(BaseUser):
    id: str


class Response(BaseModel, Generic[DataT]):
    data: DataT


@router.get('/')
def list_users() -> Response[list[User]]:
    return {
        "data": [
            {
                "name": "Ivan",
                "surname": "Ivanov",
                "age": 20,
                "address": "Moscow"
            },
            {
                "name": "Petr",
                "surname": "Petrov",
                "age": 30,
                "address": "Amsterdam"
            }
        ]
    }


@router.post('/')
def create_user(user: BaseUser, status_code=status.HTTP_201_CREATED) -> Response[User]:
    return {
        "data": {
            "id": 1,
            **user.model_dump(),
        }
    }


@router.get('/{user_id}/')
def get_user(user_id: Annotated[str, Path(min_length=6)]) -> Response[User]:
    return {
        "data": {
            "id": user_id,
            "name": "Petr",
            "surname": "Petrov",
            "age": 30,
            "address": "Amsterdam"
        }
    }


@router.put('/{user_id}/')
def update_user(user_id: Annotated[str, Path(min_length=6, title="User id")], user: User) -> Response[User]:
    return {
        "data": {
            "id": user_id,
            **user.model_dump(),
        }
    }


@router.delete('/{user_id}/')
def delete_user(user_id: Annotated[str, Path(min_length=6, title="User id")], status_code=status.HTTP_204_NO_CONTENT) -> None:
    return None
