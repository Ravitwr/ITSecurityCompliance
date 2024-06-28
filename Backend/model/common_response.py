from dataclasses import dataclass, field
from typing import Any, Optional

@dataclass
class CommonResponse:
    status: str
    errors: Optional[str] = None
    result: Any = field(default=None)

