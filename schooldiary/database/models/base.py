from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr

from core.config import conf


class SqlBaseModel(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=conf.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
