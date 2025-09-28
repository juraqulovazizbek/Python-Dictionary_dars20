def merge_dicts(a: dict, b: dict) -> dict:
    merge = a.copy()
    merge.update(b)
    return merge

# Misol
dict1 = {"name": "Ali", "age": 25}
dict2 = {"age": 30, "city": "Tashkent"}
print(merge_dicts(dict1, dict2))  # {'name': 'Ali', 'age': 30, 'city': 'Tashkent'}