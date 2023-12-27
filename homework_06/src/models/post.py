from typing import Any
from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .database import db


class TypeSafe():
    def __init__(**kwargs: Any):
        pass


class Post(db.Model, TypeSafe):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
