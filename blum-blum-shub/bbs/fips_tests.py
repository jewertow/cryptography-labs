from typing import List, TypedDict


def single_bit_test(string: List[int]) -> (int, bool):
    counter = 0
    for i in string:
        if i == 1:
            counter += 1
    return counter, 9725 < counter < 10275


def series_test(string: List[int]) -> (dict, bool):
    results = dict()
    last_value = string[0]
    counter = 0
    saved = False
    for i in string:
        if i == last_value:
            last_value = i
            counter += 1
            saved = False
        else:
            sum = results.get(counter, 0)
            results[counter] = sum + 1
            last_value = i
            counter = 1
            saved = True
    if not saved:
        sum = results.get(counter, 0)
        results[counter] = sum + 1
    return results, _verify_length_of_series(results)


def long_series_test(results: dict) -> bool:
    for key, value in results.items():
        if key >= 26:
            return False
    return True


def _verify_length_of_series(results: dict) -> bool:
    return 2315 < results.get(1, 0) < 2685 \
        and 1114 < results.get(2, 0) < 1386 \
        and 527 < results.get(3, 0) < 723 \
        and 240 < results.get(4, 0) < 384 \
        and 103 < results.get(5, 0) < 209 \
        and 103 < results.get(6, 0) < 209
