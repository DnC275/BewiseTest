from functools import lru_cache
from sqlalchemy.orm import Session

from questions import database, config


def get_db() -> Session:
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@lru_cache()
def get_db_settings() -> config.DBSettings:
    return config.DBSettings()
