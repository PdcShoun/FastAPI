from pydantic import BaseModel


class People(BaseModel):
    name: str
    age: int
