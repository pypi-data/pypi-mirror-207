__all__ = [
    "snake_case_to_pascal_case",
    "snake_case_to_camel_case",
]


def snake_case_to_pascal_case(string: str) -> str:
    return "".join([s.capitalize() for s in string.split("_")])


def snake_case_to_camel_case(string: str) -> str:
    words = [s for s in string.split("_") if s]
    return words[0] + "".join(x.title() for x in words[1:])
