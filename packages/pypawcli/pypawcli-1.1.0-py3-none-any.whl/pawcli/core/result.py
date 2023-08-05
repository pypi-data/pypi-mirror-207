from __future__ import annotations

from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Sequence
from typing import Union

from .formatter import JsonFormatter

Content = Union[Dict[str, Any], Sequence[Any], bytes]


def process_result(
    response: Content,
    formatter: Optional[Callable[[Content], str]] = None,
) -> None:  # pragma: no cover
    if formatter is None:
        formatter = JsonFormatter()
    print(formatter(response))
