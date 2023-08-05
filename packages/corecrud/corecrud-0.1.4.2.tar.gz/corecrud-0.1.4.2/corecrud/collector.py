from typing import Any

from corecrud.arguments import Argument
from corecrud.main import Main


class Collector:
    def __init__(self, query: Main) -> None:
        self.query = query

    def build(self, *arguments: Argument) -> Any:
        query = self.query.main()

        for argument in arguments:
            query = argument.query(query)

        return query
