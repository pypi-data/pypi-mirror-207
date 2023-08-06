"""Application ORM configuration."""
from __future__ import annotations

import re
from datetime import datetime
from typing import TYPE_CHECKING, Any, ClassVar, Protocol, TypeVar, runtime_checkable
from uuid import UUID, uuid4

from pydantic import AnyHttpUrl, AnyUrl, EmailStr
from sqlalchemy import MetaData, String
from sqlalchemy.event import listens_for
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    declarative_mixin,
    declared_attr,
    mapped_column,
    orm_insert_sentinel,
    registry,
)

from .types import GUID, JSON

if TYPE_CHECKING:
    from sqlalchemy.sql import FromClause

__all__ = (
    "AuditBase",
    "AuditColumns",
    "Base",
    "CommonTableAttributes",
    "create_registry",
    "ModelProtocol",
    "touch_updated_timestamp",
    "UUIDPrimaryKey",
)


BaseT = TypeVar("BaseT", bound="Base")

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
"""Templates for automated constraint name generation."""


@listens_for(Session, "before_flush")
def touch_updated_timestamp(session: Session, *_: Any) -> None:
    """Set timestamp on update.

    Called from SQLAlchemy's
    :meth:`before_flush <sqlalchemy.orm.SessionEvents.before_flush>` event to bump the ``updated``
    timestamp on modified instances.

    Args:
        session: The sync :class:`Session <sqlalchemy.orm.Session>` instance that underlies the async
            session.
    """
    for instance in session.dirty:
        if hasattr(instance, "updated"):
            instance.updated = datetime.now()  # noqa: DTZ005


@runtime_checkable
class ModelProtocol(Protocol):
    """The base SQLAlchemy model protocol."""

    __table__: FromClause
    __name__: ClassVar[str]

    def to_dict(self, exclude: set[str] | None = None) -> dict[str, Any]:
        """Convert model to dictionary.

        Returns:
            dict[str, Any]: A dict representation of the model
        """
        ...


@declarative_mixin
class UUIDPrimaryKey:
    """UUID Primary Key Field Mixin."""

    __abstract__ = True

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    """UUID Primary key column."""


@declarative_mixin
class AuditColumns:
    """Created/Updated At Fields Mixin."""

    __abstract__ = True

    created: Mapped[datetime] = mapped_column(default=datetime.now)
    """Date/time of instance creation."""
    updated: Mapped[datetime] = mapped_column(default=datetime.now)
    """Date/time of instance last update."""


@declarative_mixin
class CommonTableAttributes:
    """Common attributes for SQLALchemy tables."""

    __abstract__ = True
    __name__: ClassVar[str]
    __table__: FromClause

    # noinspection PyMethodParameters
    @declared_attr.directive
    def __tablename__(cls) -> str:  # pylint: disable=no-self-argument
        """Infer table name from class name."""
        regexp = re.compile("((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))")
        return regexp.sub(r"_\1", cls.__name__).lower()

    def to_dict(self, exclude: set[str] | None = None) -> dict[str, Any]:
        """Convert model to dictionary.

        Returns:
            dict[str, Any]: A dict representation of the model
        """
        exclude = exclude.union("_sentinel") if exclude else {"_sentinel"}
        return {field.name: getattr(self, field.name) for field in self.__table__.columns if field.name not in exclude}

    @declared_attr
    def _sentinel(cls) -> Mapped[int]:
        return orm_insert_sentinel()


def create_registry() -> registry:
    """Create a new SQLAlchemy registry."""
    meta = MetaData(naming_convention=convention)
    return registry(
        metadata=meta,
        type_annotation_map={UUID: GUID, EmailStr: String, AnyUrl: String, AnyHttpUrl: String, dict: JSON},
    )


orm_registry = create_registry()


class Base(UUIDPrimaryKey, CommonTableAttributes, DeclarativeBase):
    """Base for all SQLAlchemy declarative models."""

    registry = orm_registry


class AuditBase(CommonTableAttributes, UUIDPrimaryKey, AuditColumns, DeclarativeBase):
    """Base for declarative models with audit columns."""

    registry = orm_registry
