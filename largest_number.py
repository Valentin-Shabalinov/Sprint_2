import itertools
from typing import Optional


def largest_number(amount: Optional[int], numbers: str) -> str:
    result = []
    for permutation in itertools.permutations(str(number) for number in numbers):
        result.append(''.join(permutation))
    return max(result)


print(largest_number(input(), input()))
