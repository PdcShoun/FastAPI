from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import engine, create_engine


DATABASE_URL = "sqlite:///./sql_app.sqlite"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
