from typing import Iterator

from sqlmodel import Session, create_engine

from app.core.config import DATABASE_URL, DEBUG

# Only echo SQL statements when the app is running in debug mode.
# Echoing unconditionally leaks query contents (including user data) into
# application logs in production.
engine = create_engine(
    DATABASE_URL,
    echo=DEBUG,
    connect_args=dict(check_same_thread=False),
)


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
