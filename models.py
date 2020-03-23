import local_settings as settings
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('{}://{}:{}@{}:{}/{}').format(
    settings.DB_ENGINE,
    settings.DB_USER,
    settings.DB_PASSWORD,
    settings.DB_HOST,
    settings.DB_PORT,
    settings.DB_NAME
)


def migrate_all():
    meta = MetaData()
    meta.create_all()
