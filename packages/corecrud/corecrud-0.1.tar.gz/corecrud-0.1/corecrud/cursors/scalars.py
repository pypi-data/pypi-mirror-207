from __future__ import annotations

from typing import Any, Optional, Sequence

from corecrud.cursors.abc import ABCCursor


class Scalars(ABCCursor):
    async def one(self) -> Optional[Any]:
        return await self.result.scalars().one_or_none()

    async def many(self) -> Sequence[Any]:
        return await self.result.scalars().all()

    async def many_unique(self) -> Sequence[Any]:
        return await self.result.scalars().unique().all()
