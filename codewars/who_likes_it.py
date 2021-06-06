def execute(names: list[str]) -> str:
    if not names:
        return "no one likes this"

    size = len(names)

    if size == 1:
        return f"{names[0]} likes this"
    elif size == 2:
        return f"{names[0]} and {names[1]} like this"
    elif size == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    # should maybe be `else size >= 4:`, but mypy throws an error so have to do a bare else
    else:
        return f"{names[0]}, {names[1]} and {size - 2} others like this"
