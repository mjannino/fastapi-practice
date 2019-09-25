from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from common.config import config

engine = create_engine(config.DATABASE_CONN_STRING)

# to avoid naming collisions when type-hinting, we name this LocalSession
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def db_session(request: Request):
    return request.state.db
