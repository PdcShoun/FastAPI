from fastapi import FastAPI

from .routes import router
from .db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
