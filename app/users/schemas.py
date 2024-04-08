from pydantic import BaseModel


class UserPost(BaseModel):
    username: str
    password: str
