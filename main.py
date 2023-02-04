def words_to_uppercase(words: list[str]) -> list[str]:
    return list(map(lambda word: word.upper(), words))


# print(words_to_uppercase(['cat', 'mouse', 'cartoon']))


def raise_to_exponent(numbers: list[float]) -> list[float]:
    return list(map(lambda number: round(number ** 2, 3), numbers))


# print(raise_to_exponent([4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]))


def merge_lists(list1: list, list2: list) -> list:
    return list(zip(list1, list2))


print(merge_lists(['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4, 5]))


def filter_words_by_length(words: list[str], max_length: int) -> list[str]:
    return list(filter(lambda word: len(word) < max_length, words))


print(filter_words_by_length(["Jeff", "Alex", "Jonathan", "Richelle", "Anna"], 5))
