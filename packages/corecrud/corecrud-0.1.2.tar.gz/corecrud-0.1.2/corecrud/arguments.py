from __future__ import annotations

from typing import Any, Callable, Optional

from corecrud.typing import DictStrAny, TupleAny
from sqlalchemy import delete, insert, select, update
from sqlalchemy.sql.base import ExecutableOption, _NoArg  # noqa: W0212
from sqlalchemy.sql.dml import Insert as StandardInsert


def _build(main: Any, method: str, args: TupleAny, kwargs: DictStrAny) -> Any:
    return getattr(main, method)(*args, **kwargs)


class Collector:
    def __init__(self, query: Main) -> None:
        self.query = query

    def build(self, *arguments: Any) -> Any:
        query = self.query.main()

        for argument in arguments:
            query = argument.query(query)

        return query


class Main:
    def __init__(self, method: Any, *args: Any, **kwargs: Any) -> None:
        self.method = method

        self.args = args
        self.kwargs = kwargs

    def main(self) -> Any:
        return self.method(*self.args, **self.kwargs)


class Select(Main):
    def __init__(self, *entities: Any) -> None:
        super(Select, self).__init__(select, *entities)


class Insert(Main):
    def __init__(
        self,
        table: Any,
        *,
        dialect: Callable[..., StandardInsert] = insert,
    ) -> None:
        super(Insert, self).__init__(dialect, table)


class Update(Main):
    def __init__(self, table: Any) -> None:
        super(Update, self).__init__(update, table)


class Delete(Main):
    def __init__(self, table: Any) -> None:
        super(Delete, self).__init__(delete, table)


class Argument:
    method: str

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Object that helps to create arguments.

        :param args: arguments in method.
        :param kwargs: kwargs in method.
        """

        self.args = args
        self.kwargs = kwargs

    def query(self, main: Any) -> Any:
        return _build(main, self.method, self.args, self.kwargs)  # type: ignore[arg-type]


class Where(Argument):
    method = "where"

    def __init__(self, *whereclause: Any) -> None:
        super(Where, self).__init__(*whereclause)


class Filter(Argument):
    method = "filter"

    def __init__(self, *criteria: Any) -> None:
        super(Filter, self).__init__(*criteria)


class Join(Argument):
    method = "join"

    def __init__(
        self,
        target: Any,
        onclause: Optional[Any] = None,
        *,
        isouter: bool = False,
        full: bool = False,
    ) -> None:
        super(Join, self).__init__(
            target,
            onclause,
            isouter=isouter,
            full=full,
        )


class OuterJoin(Join):
    def __init__(
        self,
        target: Any,
        onclause: Optional[Any] = None,
        *,
        full: bool = False,
    ) -> None:
        super(OuterJoin, self).__init__(
            target,
            onclause,
            isouter=True,
            full=full,
        )


class Options(Argument):
    method = "options"

    def __init__(self, *options: ExecutableOption) -> None:
        super(Options, self).__init__(*options)


class Offset(Argument):
    method = "offset"

    def __init__(self, offset: Optional[int] = None) -> None:
        super(Offset, self).__init__(offset=offset)


class Limit(Argument):
    method = "limit"

    def __init__(self, limit: Optional[int] = None) -> None:
        super(Limit, self).__init__(limit)


class OrderBy(Argument):
    method = "order_by"

    def __init__(
        self,
        __first: Any = _NoArg.NO_ARG,
        *clauses: Any,
    ) -> None:
        super(OrderBy, self).__init__(__first, *clauses)


class GroupBy(Argument):
    method = "group_by"

    def __init__(
        self,
        __first: Any = _NoArg.NO_ARG,
        *clauses: Any,
    ) -> None:
        super(GroupBy, self).__init__(__first, *clauses)


class Having(Argument):
    method = "having"

    def __init__(self, *having: Any) -> None:
        super(Having, self).__init__(*having)


class SelectFrom(Argument):
    method = "select_from"

    def __init__(self, *froms: Any) -> None:
        super(SelectFrom, self).__init__(*froms)


class Correlate(Argument):
    method = "correlate"

    def __init__(self, *fromclauses: Any) -> None:
        super(Correlate, self).__init__(*fromclauses)


class Values(Argument):
    method = "values"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Values, self).__init__(*args, **kwargs)


class Returning(Argument):
    method = "returning"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Returning, self).__init__(*args, **kwargs)
