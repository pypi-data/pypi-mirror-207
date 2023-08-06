from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from plutous.config import config


if config.db is None:
    raise ValueError("Database config is not set")

engine = create_engine(
    URL.create(
        drivername="postgresql+psycopg2",
        username=config.db.user,
        password=config.db.password,
        host=config.db.host,
        port=config.db.port,
        database=config.db.db,
    )
)
