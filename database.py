from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine =create_async_engine("sqlite+aiosqlite:///test.db", echo=True)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[Optional[str]] = mapped_column(nullable=True)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_db():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)