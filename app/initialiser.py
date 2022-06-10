from app.database.initialise import initialise
from app.database.session import SessionLocal
from alembic.config import Config
from alembic.command import upgrade
from app.core.config import settings


def init() -> None:
    db = SessionLocal()
    initialise(db)
    upgrade(Config(settings.ALEMBIC_INI), "head")


def main() -> None:
    init()


if __name__ == "__main__":
    main()
