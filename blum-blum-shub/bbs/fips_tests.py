from typing import List


def single_bit_test(string: List[int]) -> (int, bool):
    counter = 0
    for i in string:
        if i == 1:
            counter += 1
    return counter, 9725 < counter < 10275
