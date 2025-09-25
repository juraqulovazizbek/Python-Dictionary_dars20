from pprint import pprint as pp


person = {
    "name": "Ali",
    "age": 25,
    "city": "Tashkent"
}

element = person.pop("city")
print(f"o'chirildi {element}" )
print(person)
