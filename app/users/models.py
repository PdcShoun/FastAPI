from ..db.database import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column, Mapped


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    username: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )
    password: Mapped[str] = mapped_column(
        nullable=False,
    )
