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
        *arguments: Argument,
        nested_select: Optional[Sequence[Any]] = None,
    ) -> Any:
        nested_select = [] if not nested_select else nested_select

        collector = Collector(SelectMain(self.model, *nested_select))
        return collector.build(*arguments)


class SelectExecutor(_Executor[ModelT], Generic[ModelT]):
    def __init__(self, model: Type[ModelT]) -> None:
        super(SelectExecutor, self).__init__(query=SelectQuery(model=model))

    async def execute(
        self,
        *arguments: Argument,
        session: AsyncSession,
        nested_select: Optional[Sequence[Any]] = None,
    ) -> AsyncResult[Any]:
        return await session.stream(self.query.build(*arguments, nested_select=nested_select))


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
        *arguments: Argument,
        session: AsyncSession,
        nested_select: Optional[Sequence[Any]] = None,
    ) -> Optional[ModelT]:
        return await super(Select, self).one(
            *arguments, session=session, nested_select=nested_select
        )

    async def many(
        self,
        *arguments: Argument,
        session: AsyncSession,
        nested_select: Optional[Sequence[Any]] = None,
    ) -> Sequence[ModelT]:
        return await super(Select, self).many(
            *arguments, session=session, nested_select=nested_select
        )

    async def many_unique(
        self,
        *arguments: Argument,
        session: AsyncSession,
        nested_select: Optional[Sequence[Any]] = None,
    ) -> Sequence[ModelT]:
        return await super(Select, self).many_unique(
            *arguments, session=session, nested_select=nested_select
        )


class InsertQuery(_ABCQuery[ModelT]):
    def build(
        self,
        *arguments: Argument,
        dialect: Any = insert,
    ) -> Any:
        collector = Collector(InsertMain(self.model, dialect=dialect))
        return collector.build(*arguments)


class InsertExecutor(_Executor[ModelT], Generic[ModelT]):
    def __init__(self, model: Type[ModelT]) -> None:
        super(InsertExecutor, self).__init__(query=InsertQuery(model=model))

    async def execute(
        self,
        *arguments: Argument,
        session: AsyncSession,
        dialect: Any = insert,
    ) -> AsyncResult[Any]:
        return await session.stream(self.query.build(*arguments, dialect=dialect))


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
        *arguments: Argument,
        session: AsyncSession,
        dialect: Any = insert,
    ) -> Optional[ModelT]:
        return await super(Insert, self).one(*arguments, session=session, dialect=dialect)

    async def many(
        self,
        *arguments: Argument,
        session: AsyncSession,
        dialect: Any = insert,
    ) -> Sequence[ModelT]:
        return await super(Insert, self).many(*arguments, session=session, dialect=dialect)

    async def many_unique(
        self,
        *arguments: Argument,
        session: AsyncSession,
        dialect: Any = insert,
    ) -> Sequence[ModelT]:
        return await super(Insert, self).many_unique(*arguments, session=session, dialect=dialect)


class UpdateQuery(_ABCQuery[ModelT]):
    def build(self, *arguments: Argument) -> Any:
        collector = Collector(UpdateMain(self.model))
        return collector.build(*arguments)


class UpdateExecutor(_Executor[ModelT], Generic[ModelT]):
    def __init__(self, model: Type[ModelT]) -> None:
        super(UpdateExecutor, self).__init__(query=UpdateQuery(model=model))

    async def execute(
        self,
        *arguments: Argument,
        session: AsyncSession,
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
        *arguments: Argument,
        session: AsyncSession,
    ) -> Optional[ModelT]:
        return await super(Update, self).one(*arguments, session=session)

    async def many(
        self,
        *arguments: Argument,
        session: AsyncSession,
    ) -> Sequence[ModelT]:
        return await super(Update, self).many(*arguments, session=session)

    async def many_unique(
        self,
        *arguments: Argument,
        session: AsyncSession,
    ) -> Sequence[ModelT]:
        return await super(Update, self).many_unique(*arguments, session=session)


class DeleteQuery(_ABCQuery[ModelT]):
    def build(self, *arguments: Argument) -> Any:
        collector = Collector(DeleteMain(self.model))
        return collector.build(*arguments)


class DeleteExecutor(_Executor[ModelT], Generic[ModelT]):
    def __init__(self, model: Type[ModelT]) -> None:
        super(DeleteExecutor, self).__init__(query=DeleteQuery(model=model))

    async def execute(
        self,
        *arguments: Argument,
        session: AsyncSession,
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
        *arguments: Argument,
        session: AsyncSession,
    ) -> Optional[ModelT]:
        return await super(Delete, self).one(*arguments, session=session)

    async def many(
        self,
        *arguments: Argument,
        session: AsyncSession,
    ) -> Sequence[ModelT]:
        return await super(Delete, self).many(*arguments, session=session)

    async def many_unique(
        self,
        *arguments: Argument,
        session: AsyncSession,
    ) -> Sequence[ModelT]:
        return await super(Delete, self).many_unique(*arguments, session=session)


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
