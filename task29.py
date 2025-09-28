def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    active = []

    for user in users.values():
     if user["active"]: active.append(user["name"])

    return active

users = {
    "u1": {"name": "Ali", "active": True},
    "u2": {"name": "Vali", "active": False},
    "u3": {"name": "Sami", "active": True}
}

print(get_active_users(users))
