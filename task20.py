from pprint import pprint

permissions = {
"read": True,
 "write": False,
 "delete": True
 }

for key in permissions:
    if permissions[key]:
        print(key)