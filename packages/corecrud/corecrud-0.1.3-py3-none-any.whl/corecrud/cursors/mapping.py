from __future__ import annotations

from typing import Any, Optional, Sequence

from corecrud.cursors.abc import ABCCursor


class Mappings(ABCCursor):
    async def one(self) -> Optional[Any]:
        return await self.result.mappings().one_or_none()

    async def many(self) -> Sequence[Any]:
        return await self.result.mappings().all()

    async def many_unique(self) -> Sequence[Any]:
        return await self.result.mappings().unique().all()
