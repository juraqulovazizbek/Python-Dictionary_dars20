from pprint import pprint as pr

def group_by_length(words: list[str]) -> dict[int, list[str]]:
    new_dict = {}

    for word in words:
        new_dict.setdefault(len(word), []).append(word)

    return new_dict

words = ["apple", "bat", "cat", "banana", "dog", "egg"]
pr(group_by_length(words))