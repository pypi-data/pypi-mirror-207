from __future__ import annotations

import abc
from typing import Any, Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncResult


class ABCCursor(abc.ABC):
    def __init__(self, result: AsyncResult[Any]) -> None:
        self.result = result

    @abc.abstractmethod
    async def one(self) -> Optional[Any]:
        ...

    @abc.abstractmethod
    async def many(self) -> Sequence[Any]:
        ...

    @abc.abstractmethod
    async def many_unique(self) -> Sequence[Any]:
        ...
