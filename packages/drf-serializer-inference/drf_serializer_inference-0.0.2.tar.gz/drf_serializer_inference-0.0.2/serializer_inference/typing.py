from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ForwardRef,
    Literal,
    Optional,
    TypedDict,
    TypeVar,
    Union,
    _eval_type,  # type: ignore
    get_args,
    get_origin,
)

# New in version 3.10
try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

__all__ = [
    "Any",
    "Callable",
    "eval_type",
    "ForwardRef",
    "get_args",
    "get_origin",
    "Literal",
    "Optional",
    "TYPE_CHECKING",
    "TypedDict",
    "TypesDict",
    "TypeVar",
    "Union",
]

eval_type = _eval_type
TypesDict: TypeAlias = dict[str, Union[Optional[type], "TypesDict"]]  # type: ignore
