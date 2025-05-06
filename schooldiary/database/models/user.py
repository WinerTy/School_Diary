from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from .base import SqlBaseModel
from .mixins.id_mixin import IdMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(SqlBaseModel, IdMixin, SQLAlchemyBaseUserTable[int]):
    first_name: Mapped[str] = mapped_column(String(128), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(128), nullable=True)
    last_name: Mapped[str] = mapped_column(String(128), nullable=False)

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name if self.middle_name else ''} {self.last_name}"

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)

    def __str__(self):
        return self.full_name

    # async def __admin_repr__(self, request: Request) -> str:
    #     return self.full_name
    #
    # async def __admin_select2_repr__(self, request: Request) -> str:
    #     template = Template(
    #         """<span>{{ full_name }}</span>""",
    #         autoescape=True,
    #     )
    #     return template.render(full_name=self.full_name)
