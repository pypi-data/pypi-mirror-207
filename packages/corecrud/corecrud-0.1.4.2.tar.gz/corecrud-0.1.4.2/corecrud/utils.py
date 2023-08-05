from typing import Any

from corecrud.typing import DictStrAny, TupleAny


def filter_none(collection: TupleAny) -> TupleAny:
    return (element for element in collection if element is not None)


def call_next(main: Any, method: str, args: TupleAny, kwargs: DictStrAny) -> Any:
    return getattr(main, method)(*args, **kwargs)
