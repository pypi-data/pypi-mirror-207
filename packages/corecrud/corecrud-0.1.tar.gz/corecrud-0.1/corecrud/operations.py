from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Any, Generic, Optional, Sequence, Type, TypeVar

from corecrud.arguments import Collector
from corecrud.arguments import Delete as DeleteMain
from corecrud.arguments import Insert as InsertMain
from corecrud.arguments import Select as SelectMain
from corecrud.arguments import Update as UpdateMain
from corecrud.cursors import Scalars
from corecrud.cursors.abc import ABCCursor
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncResult, AsyncSession

ModelT = TypeVar("ModelT")

if TYPE_CHECKING:
    from corecrud.arguments import Argument


class _ABCQuery(abc.ABC, Generic[ModelT]):
    def __init__(self, model: Type[ModelT]) -> None:
        self.model = model

    @abc.abstractmethod
    def build(self, *args: Any, **kwargs: Any) -> Any:
        ...


class _Executor(abc.ABC, Generic[ModelT]):
    def __init__(self, query: _ABCQuery[ModelT]) -> None:
        self.query = query

    @abc.abstractmethod
    async def execute(self, *args: Any, **kwargs: Any) -> AsyncResult[Any]:
        ...


class CRUDOperation(abc.ABC, Generic[ModelT]):
    def __init__(
        self,
        cursor_cls: Type[ABCCursor] = Scalars,
        *,
        executor: _Executor[ModelT],
    ) -> None:
        self.cursor_cls = cursor_cls
        self.executor = executor

    async def one(self, *args: Any, **kwargs: Any) -> Optional[ModelT]:
        cursor = self.cursor_cls(await self.executor.execute(*args, **kwargs))
        return await cursor.one()

    async def many(self, *args: Any, **kwargs: Any) -> Sequence[ModelT]:
        cursor = self.cursor_cls(await self.executor.execute(*args, **kwargs))
        return await cursor.many()

    async def many_unique(self, *args: Any, **kwargs: Any) -> Sequence[ModelT]:
        cursor = self.cursor_cls(await self.executor.execute(*args, **kwargs))
        return await cursor.many_unique()


class SelectQuery(_ABCQuery[ModelT]):
    def build(
        self,
        nested_select: Optional[Sequence[Any]] = None,
        *arguments: Argument,
    ) -> Any:
        collector = Collector(SelectMain(self.model))
        return collector.build(*arguments)


class SelectExecutor(_Executor[ModelT], Generic[ModelT]):
    def __init__(self, model: Type[ModelT]) -> None:
        super(SelectExecutor, self).__init__(query=SelectQuery(model=model))

    async def execute(
        self,
        session: AsyncSession,
        nested_select: Optional[Sequence[Any]] = None,
        *arguments: Argument,
    ) -> AsyncResult[Any]:
        return await session.stream(self.query.build(nested_select=nested_select, *arguments))


class Select(CRUDOperation[ModelT]):
    def __init__(
        self,
        model: Type[ModelT],
        *,
        cursor_cls: Type[ABCCursor] = Scalars,
    ) -> None:
        super(Select, self).__init__(
            cursor_cls=cursor_cls,
            executor=SelectExecutor(model=model),
        )

    async def one(
        self,
        session: AsyncSession,
        nested_select: Optional[Sequence[Any]] = None,
        *arguments: Argument,
    ) -> Optional[ModelT]:
        return await super(Select, self).one(session, nested_select=nested_select, *arguments)

    async def many(
        self,
        session: AsyncSession,
        nested_select: Optional[Sequence[Any]] = None,
        *arguments: Argument,
    ) -> Sequence[ModelT]:
        return await super(Select, self).many(session, nested_select=nested_select, *arguments)

    async def many_unique(
        self,
        session: AsyncSession,
        nested_select: Optional[Sequence[Any]] = None,
        *arguments: Argument,
    ) -> Sequence[ModelT]:
        return await super(Select, self).many_unique(
            session, nested_select=nested_select, *arguments
        )


class InsertQuery(_ABCQuery[ModelT]):
    def build(
        self,
        dialect: Any = insert,
        *arguments: Argument,
    ) -> Any:
        collector = Collector(InsertMain(self.model, dialect=dialect))
        return collector.build(*arguments)


class InsertExecutor(_Executor[ModelT], Generic[ModelT]):
    def __init__(self, model: Type[ModelT]) -> None:
        super(InsertExecutor, self).__init__(query=InsertQuery(model=model))

    async def execute(
        self,
        session: AsyncSession,
        dialect: Any = insert,
        *arguments: Argument,
    ) -> AsyncResult[Any]:
        return await session.stream(self.query.build(dialect=dialect, *arguments))


class Insert(CRUDOperation[ModelT]):
    def __init__(
        self,
        model: Type[ModelT],
        *,
        cursor_cls: Type[ABCCursor] = Scalars,
    ) -> None:
        super(Insert, self).__init__(
            cursor_cls=cursor_cls,
            executor=InsertExecutor(model=model),
        )

    async def one(
        self,
        session: AsyncSession,
        dialect: Any = insert,
        *arguments: Argument,
    ) -> Optional[ModelT]:
        return await super(Insert, self).one(session, dialect=dialect, *arguments)

    async def many(
        self,
        session: AsyncSession,
        dialect: Any = insert,
        *arguments: Argument,
    ) -> Sequence[ModelT]:
        return await super(Insert, self).many(session, dialect=dialect, *arguments)

    async def many_unique(
        self,
        session: AsyncSession,
        dialect: Any = insert,
        *arguments: Argument,
    ) -> Sequence[ModelT]:
        return await super(Insert, self).many_unique(session, dialect=dialect, *arguments)


class UpdateQuery(_ABCQuery[ModelT]):
    def build(
        self,
        *arguments: Argument,
    ) -> Any:
        collector = Collector(UpdateMain(self.model))
        return collector.build(*arguments)


class UpdateExecutor(_Executor[ModelT], Generic[ModelT]):
    def __init__(self, model: Type[ModelT]) -> None:
        super(UpdateExecutor, self).__init__(query=UpdateQuery(model=model))

    async def execute(
        self,
        session: AsyncSession,
        *arguments: Argument,
    ) -> AsyncResult[Any]:
        return await session.stream(self.query.build(*arguments))


class Update(CRUDOperation[ModelT]):
    def __init__(
        self,
        model: Type[ModelT],
        *,
        cursor_cls: Type[ABCCursor] = Scalars,
    ) -> None:
        super(Update, self).__init__(
            cursor_cls=cursor_cls,
            executor=UpdateExecutor(model=model),
        )

    async def one(
        self,
        session: AsyncSession,
        *arguments: Argument,
    ) -> Optional[ModelT]:
        return await super(Update, self).one(session, *arguments)

    async def many(
        self,
        session: AsyncSession,
        *arguments: Argument,
    ) -> Sequence[ModelT]:
        return await super(Update, self).many(session, *arguments)

    async def many_unique(
        self,
        session: AsyncSession,
        *arguments: Argument,
    ) -> Sequence[ModelT]:
        return await super(Update, self).many_unique(session, *arguments)


class DeleteQuery(_ABCQuery[ModelT]):
    def build(self, *arguments: Argument) -> Any:
        collector = Collector(DeleteMain(self.model))
        return collector.build(*arguments)


class DeleteExecutor(_Executor[ModelT], Generic[ModelT]):
    def __init__(self, model: Type[ModelT]) -> None:
        super(DeleteExecutor, self).__init__(query=DeleteQuery(model=model))

    async def execute(
        self,
        session: AsyncSession,
        *arguments: Argument,
    ) -> AsyncResult[Any]:
        return await session.stream(self.query.build(*arguments))


class Delete(CRUDOperation[ModelT]):
    def __init__(
        self,
        model: Type[ModelT],
        *,
        cursor_cls: Type[ABCCursor] = Scalars,
    ) -> None:
        super(Delete, self).__init__(
            cursor_cls=cursor_cls,
            executor=DeleteExecutor(model=model),
        )

    async def one(
        self,
        session: AsyncSession,
        *arguments: Argument,
    ) -> Optional[ModelT]:
        return await super(Delete, self).one(session, *arguments)

    async def many(
        self,
        session: AsyncSession,
        *arguments: Argument,
    ) -> Sequence[ModelT]:
        return await super(Delete, self).many(session, *arguments)

    async def many_unique(
        self,
        session: AsyncSession,
        *arguments: Argument,
    ) -> Sequence[ModelT]:
        return await super(Delete, self).many_unique(session, *arguments)


class CRUD(Generic[ModelT]):
    def __init__(
        self,
        model: Type[ModelT],
        *,
        cursor_cls: Type[ABCCursor] = Scalars,
        select: Type[Select[ModelT]] = Select,
        insert: Type[Insert[ModelT]] = Insert,
        update: Type[Update[ModelT]] = Update,
        delete: Type[Delete[ModelT]] = Delete,
    ) -> None:
        self.select = select(model=model, cursor_cls=cursor_cls)
        self.insert = insert(model=model, cursor_cls=cursor_cls)
        self.update = update(model=model, cursor_cls=cursor_cls)
        self.delete = delete(model=model, cursor_cls=cursor_cls)
