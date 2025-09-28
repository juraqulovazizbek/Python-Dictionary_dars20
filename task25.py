def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    group_age = {}
    for odam in people:
        group_age.setdefault(odam["age"] , []).append(odam["name"])
    
    return group_age



persons = [
    {
        "name": "ali",
        "age": 12
    },
    {
        "name": "vali",
        "age": 14
    },
    {
        "name": "gani",
        "age": 12
    },
    {
        "name": "smai",
        "age": 19
    },
]
odam = group_by_age(persons)
print(odam)