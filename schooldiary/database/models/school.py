from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database.models import SqlBaseModel
from database.models.mixins.id_mixin import IdMixin


class School(SqlBaseModel, IdMixin):
    name: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
