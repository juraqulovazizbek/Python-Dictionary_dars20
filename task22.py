from pprint import pprint as pr

def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    talaba = dict()

    for student in students:
     talaba.setdefault(student["group"], []).append(student["name"])

    return talaba

students = [
    {"name": "Ali", "group": "A"},
    {"name": "Soli", "group": "A"},
    {"name": "Vali", "group": "B"},
    {"name": "Karim", "group": "B"},
    {"name": "Dilnoza", "group": "C"},
    {"name": "Aziza", "group": "C"},
    {"name": "Jasur", "group": "A"},
    {"name": "Malika", "group": "B"},
]

student = group_students(students)
pr(student)
