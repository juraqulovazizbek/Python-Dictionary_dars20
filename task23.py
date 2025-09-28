from pprint import pprint as pr

def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group = dict()

    for az, num in enumerate(numbers):
     group.setdefault(num , []).append(az)

    return group


numbers = [3, 5, 3, 2, 5, 3,56,63,33,335,55,8,9,35,41,7,1,23,33,99,5,2,3,7,4,]

pr(group_indices(numbers))
