from datetime import date, datetime, time, timedelta
from decimal import Decimal
from inspect import getfullargspec
from typing import Dict, List, Set, Tuple, Type

from rest_framework.fields import (
    BooleanField,
    CharField,
    ChoiceField,
    DateField,
    DateTimeField,
    DecimalField,
    DictField,
    DurationField,
    Field,
    FloatField,
    IntegerField,
    JSONField,
    ListField,
    TimeField,
)
from rest_framework.serializers import ListSerializer, Serializer

from .typing import (
    Any,
    Callable,
    ForwardRef,
    Literal,
    Optional,
    TypesDict,
    TypeVar,
    Union,
    eval_type,
    get_args,
    get_origin,
)
from .utils import snake_case_to_pascal_case

__all__ = [
    "inline_serializer",
    "serializer_from_callable",
]


TSerializer = TypeVar("T", bound=Serializer)


def serializer_from_callable(func: Callable[..., Any], output: bool = False) -> type[Serializer]:
    """Create a serializer from the parameter type hints of a callable.
    Attempt to infer the types from the default arguments if no typing information is available.
    If output is true, infer from callable return type.
    In this case, return type should be a TypedDict so that field conversion works.
    """
    types = _return_types(func) if output else _parameter_types(func)
    is_list = isinstance(types, list)
    fields = _get_fields(types[0]) if is_list else _get_fields(types)
    serializer_name = snake_case_to_pascal_case(f"{func.__name__}_serializer")
    return inline_serializer(serializer_name, fields=fields, many=is_list)


def inline_serializer(
    name: str,
    super_class: type[TSerializer] = Serializer,
    fields: dict[str, Field] = None,
    many: bool = False,
) -> type[TSerializer]:
    serializer: type[TSerializer] = type(name, (super_class,), fields or {})  # type: ignore
    serializer.many = many
    return serializer


def _parameter_types(func: Callable[..., Any]) -> TypesDict:
    """Get the types for a callable's parameters."""
    func = _unwrap_function(func)
    args_spec = getfullargspec(func)
    types = args_spec.annotations
    types.pop("return", None)

    # Get types based on argument default values
    defaults: tuple[Any, ...] = args_spec.defaults or ()
    for name, value in zip(reversed(args_spec.args), reversed(defaults)):  # noqa
        if name in types:
            continue
        types[name] = type(value)

    # Get types based on keyword-only argument default values
    defaults_kwonly: dict[str, Any] = args_spec.kwonlydefaults or {}
    for name, value in defaults_kwonly.items():
        if name in types:
            continue
        types[name] = type(value)

    # Add None for all positional arguments and keyword-only arguments
    # for which a type was not found or could not be inferred
    for name in args_spec.args + args_spec.kwonlyargs:
        if name in types:
            continue
        types[name] = None

    # Remove * and ** parameters from the typing dict
    types.pop(args_spec.varargs or "", None)
    types.pop(args_spec.varkw or "", None)

    global_namespace = _get_globals(func)
    for name, type_ in types.items():
        types[name] = _unwrap_types(type_, global_namespace)

    return types


def _return_types(func: Callable[..., Any]) -> Union[TypesDict, list[TypesDict]]:
    """Get the callables return types"""
    func = _unwrap_function(func)
    args_spec = getfullargspec(func)
    return_type = args_spec.annotations.get("return")
    return _unwrap_types(return_type, _get_globals(func))


_type_to_serializer_field: dict[Optional[type], type[Field]] = {
    str: CharField,
    int: IntegerField,
    float: FloatField,
    bool: BooleanField,
    dict: DictField,
    list: ListField,
    date: DateField,
    datetime: DateTimeField,
    time: TimeField,
    timedelta: DurationField,
    Decimal: DecimalField,
    None: CharField,
    type: CharField,
}
_standard_generics_to_typing_equivalents: dict[str, type] = {
    "list": List[Any],
    "set": Set[Any],
    "tuple": Tuple[Any],
    "dict": Dict[Any, Any],
    "type": Type[Any],
}


def _get_fields(types: TypesDict) -> dict[str, Field]:
    """Convert types to serializer fields.
    TypedDicts and other classes with __annotations__ dicts
    are recursively converted to serializers based on their types.
    """

    fields: dict[str, Field] = {}
    for name, type_ in types.items():
        # Could not determine forward referenced TypedDict
        # from another file. This is the best guess.
        if isinstance(type_, ForwardRef):
            fields[name] = JSONField()
            continue

        if isinstance(type_, dict):
            fields[name] = inline_serializer(name, fields=_get_fields(type_))()
            continue

        if isinstance(type_, list):
            if isinstance(type_[0], dict):
                fields[name] = inline_serializer(name, fields=_get_fields(type_[0]))(many=True)
            else:
                fields[name] = ListField(child=_type_to_serializer_field.get(type_[0], CharField)())

            continue

        if get_origin(type_) == Literal:
            choices = [arg.__forward_arg__ for arg in get_args(type_)]
            fields[name] = ChoiceField(choices=choices)
            continue

        field = _type_to_serializer_field.get(type_, CharField)
        if issubclass(field, DecimalField):
            fields[name] = field(max_digits=13, decimal_places=3)
            continue

        fields[name] = field()

    return fields


def _unwrap_types(
    types: Union[type, TypesDict, list[TypesDict]],
    global_namespace: dict[str, Any],
) -> Union[type, TypesDict, list[TypesDict]]:
    """Recursively unwrap types from the given item."""
    typ = _forward_refs_to_types(types, global_namespace)

    if hasattr(typ, "__origin__"):
        return _unwrap_generic(typ, global_namespace)

    if not hasattr(typ, "__annotations__"):
        return typ

    annotations: TypesDict = typ.__annotations__
    for name, annotation in annotations.items():
        annotations[name] = _unwrap_types(annotation, global_namespace)

    return annotations


def _forward_refs_to_types(
    types: Union[type, TypesDict, list[TypesDict]],
    global_namespace: dict[str, Any],
) -> Union[type, TypesDict, list[TypesDict]]:
    """Convert strings and forward references to types."""
    if isinstance(types, str):
        types = ForwardRef(types)

    if isinstance(types, ForwardRef):
        try:
            types = eval_type(types, global_namespace, global_namespace)
        except NameError:
            pass

    if hasattr(types, "__args__"):
        args = []
        for arg in types.__args__:
            args.append(_forward_refs_to_types(arg, global_namespace))
        types = _standard_generics_to_typing_equivalents.get(getattr(types, "__qualname__", types), types)
        types.__args__ = tuple(args)

    return types


def _unwrap_generic(
    type_: type, global_namespace: dict[str, Any]
) -> Union[list[TypesDict], dict[str, list[TypesDict]], type]:
    """Unwrap the arguments of generics like list and dicts into proper types."""
    origin_type: type = get_origin(type_)
    origin_args: tuple[type, ...] = get_args(type_)
    special_type = origin_type in (Union,)

    try:
        if not issubclass(origin_type, (tuple, list, set, dict)):  # pragma: no cover
            return type_
    except TypeError:
        if not special_type:
            return type_

    if not special_type and issubclass(origin_type, dict):
        origin_args = origin_args[1:]

    arg_types = _get_arg_types(origin_args, global_namespace)

    if origin_type == Union:
        return arg_types[0]

    if issubclass(origin_type, dict):
        return {"str": arg_types[0]}

    return arg_types


def _get_arg_types(
    origin_args: tuple[type, ...],
    global_namespace: dict[str, Any],
) -> Union[list[TypesDict], dict[str, list[TypesDict]], type]:
    arg_types = []

    for arg_type in origin_args:
        arg_type = _forward_refs_to_types(arg_type, global_namespace)

        if not hasattr(arg_type, "__annotations__"):
            if hasattr(arg_type, "__origin__"):
                arg_type = _unwrap_generic(arg_type, global_namespace)

            arg_types.append(arg_type)
            continue

        annotations = {}
        for name, annotation in arg_type.__annotations__.items():
            annotations[name] = _unwrap_types(annotation, global_namespace)

        arg_types.append(annotations)

    return arg_types


def _unwrap_function(func: Callable[..., Any]) -> Callable[..., Any]:
    """Unwrap decorated functions to allow fetching types from them."""
    while hasattr(func, "__wrapped__"):
        func = func.__wrapped__
    return func


def _get_globals(func: Callable[..., Any]) -> dict[str, Any]:
    return getattr(_unwrap_function(func), "__globals__", {})


def _to_comparable_dict(serializer: Serializer) -> dict[str, Any]:
    dct = {}
    is_list = isinstance(serializer, ListSerializer)
    fields = serializer.child.fields if is_list else serializer.fields
    for name, field in fields.items():
        if isinstance(field, ListSerializer):
            dct[name] = [_to_comparable_dict(field.child)]
        elif isinstance(field, Serializer):
            dct[name] = _to_comparable_dict(field)
        else:
            dct[name] = str(field)
    return [dct] if is_list else dct
