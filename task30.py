def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    result = {}
    for k, v in d.items():
        if v != 0:
            result[k] = v
    return result

data = {"a": 5, "b": 0, "c": 3, "d": 0}
print(filter_non_zero(data))
