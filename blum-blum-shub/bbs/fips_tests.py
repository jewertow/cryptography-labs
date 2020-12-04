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
    _verify_correctness(results)
    return results, _verify_length_of_series(results)


def long_series_test(series_counters: dict) -> bool:
    for series_length, _ in series_counters.items():
        if series_length >= 26:
            return False
    return True


def poker_test(string: List[int]) -> (float, bool):
    segments = _divide_into_segments(string)
    int_values = _segments_to_int_values(segments)
    counters = dict()
    for i in int_values:
        counters[i] = counters.get(i, 0) + 1
    sorted_counters = dict(sorted(counters.items()))
    sorted_counters = list(sorted_counters.values())
    poker_test_value = _calculate_x(sorted_counters)
    return poker_test_value, 2.16 < poker_test_value < 46.17


def _divide_into_segments(string: List[int]) -> List[List[int]]:
    return [
        string[i: i+4] for i in range(0, len(string), 4)
    ]


def _segments_to_int_values(segments: List[List[int]]) -> List[int]:
    int_values = []
    for segment in segments:
        # [1, 1, 0, 1] => '1101'
        string_binary_value = ''.join(str(i) for i in segment)
        # '1101' => 13
        int_value = int(string_binary_value, 2)
        int_values.append(int_value)
    return int_values


def _calculate_x(sorted_counter: List[int]) -> float:
    sum = 0
    for counter in sorted_counter:
        sum += counter ** 2
    return (16 / 5000) * sum - 5000


def _verify_correctness(results: dict):
    series_counter_sum = 0
    for key, value in results.items():
        series_counter_sum += (key * value)
    if series_counter_sum != 20_000:
        raise RuntimeError(f'Sum of series counters is not equal to 20 000!.'
                           f'\nsum = {series_counter_sum}\nresults = {results}')


def _verify_length_of_series(results: dict) -> bool:
    return 2315 < results.get(1, 0) < 2685 \
        and 1114 < results.get(2, 0) < 1386 \
        and 527 < results.get(3, 0) < 723 \
        and 240 < results.get(4, 0) < 384 \
        and 103 < results.get(5, 0) < 209 \
        and 103 < results.get(6, 0) < 209
