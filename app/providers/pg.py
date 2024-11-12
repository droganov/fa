from psycopg_pool import AsyncConnectionPool
from typing import TypeVar, AsyncGenerator, Any, List, Type
from contextlib import asynccontextmanager
from pydantic import BaseModel
from psycopg import AsyncConnection, AsyncCursor, AsyncClientCursor
from psycopg.rows import AsyncRowFactory, TupleRow, class_row

from app.config import config


class Tag(BaseModel):
    group: str


ProducedRow = TypeVar("ProducedRow")
QueryResult = TypeVar("QueryResult", bound=BaseModel)


@asynccontextmanager
async def pg_connection() -> AsyncGenerator[AsyncConnection, Any]:
    async with AsyncConnectionPool(
        check=AsyncConnectionPool.check_connection,
        conninfo=config.database_url,
        max_lifetime=600,
    ) as async_pool:
        async with async_pool.connection() as conn:
            yield conn


@asynccontextmanager
async def pg_cursor(
    **kwargs: Any,
) -> AsyncGenerator[AsyncCursor[TupleRow], Any]:
    async with pg_connection() as conn:
        async with conn.cursor(**kwargs) as cur:
            yield cur


@asynccontextmanager
async def pg_model(
    row_factory: AsyncRowFactory[ProducedRow],
    **kwargs: Any,
) -> AsyncGenerator[AsyncCursor[ProducedRow], Any]:
    async with pg_connection() as conn:
        async with conn.cursor(row_factory=row_factory, **kwargs) as cur:
            yield cur


async def pg_fetch_some(
    query: str,
    values: dict[str, Any],
    Model: Type[QueryResult],
    **kwargs: Any,
) -> List[QueryResult]:
    async with pg_model(row_factory=class_row(Model), **kwargs) as cur:
        await cur.execute(query, values)
        result = await cur.fetchall()
        return result


async def pg_fetch_one(
    query: str,
    values: dict[str, Any],
    Model: Type[QueryResult],
    **kwargs: Any,
) -> QueryResult | None:
    async with pg_model(row_factory=class_row(Model), **kwargs) as cur:
        await cur.execute(query, values)
        result = await cur.fetchone()
        return result


async def pg_fetch_val(
    query: str,
    values: dict[str, Any],
    **kwargs: Any,
) -> Any:
    async with pg_cursor(**kwargs) as cur:
        await cur.execute(query, values)
        result = await cur.fetchone()
        if not result:
            return None
        return result[0]


async def pg_execute(
    query: str,
    values: dict[str, Any],
    **kwargs: Any,
) -> None:
    async with pg_cursor(**kwargs) as cur:
        await cur.execute(query, values)


async def pg_transaction(
    query: str,
    values: dict[str, Any],
) -> Any:
    async with pg_connection() as conn:
        try:
            return await AsyncClientCursor(conn).execute(query, values)
        finally:
            await conn.close()
