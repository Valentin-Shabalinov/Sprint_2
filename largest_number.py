import itertools
from typing import Optional


def largest_number(amount: Optional[int], numbers: str) -> str:
    result = []
    for number in numbers:
        for permutation in itertools.permutations(str(number)):
            result.append(''.join(permutation))
        return max(result)


print(largest_number(input(), input()))
