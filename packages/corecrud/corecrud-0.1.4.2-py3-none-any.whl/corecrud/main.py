from typing import Any, Callable

from corecrud.utils import filter_none
from sqlalchemy import delete, insert, select, update
from sqlalchemy.sql.dml import Insert as StandardInsert


class Main:
    def __init__(self, method: Any, *args: Any, **kwargs: Any) -> None:
        self.method = method

        self.args = filter_none(args)
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
