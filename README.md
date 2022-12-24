## 1 - Правильные скобочные последовательности
Необходимо реализовать функцию, генерирующую скобочную последовательность, в зависимости от входного параметра ( n = 0...10 )
Правило генерации следующее:
- “(” должна идти раньше “)”
- Длина последовательности 2n
- Необходимо выполнить перебор всевозможных вариантов в лексикографическом порядке
### Решение
```
import itertools


def is_correct_brackets(text):
    while '()' in text:
        text = text.replace('()', '')

    return not text


def largest_number(input_parameter: int) -> str:

    result = []
    subseq = input_parameter * str('()')
    for permutation in itertools.permutations(bracket for bracket in subseq):
        result.append(''.join(permutation))

    possible_options = []
    for option in set(result):
        if is_correct_brackets(option):
            possible_options.append(option)

    return possible_options


print(largest_number(int(input())))

```


## 2 - Составить самое большое число
#### Необходимо составить наибольшее число из числа предложенных. На вход поступает два параметра:
- количество чисел n ≤ 100
- строка с n числами, записанными через пробел. Каждое отдельное число не превосходит 1000
### Решение
```
import itertools
from typing import Optional


def largest_number(amount: Optional[int], numbers: str) -> str:
    result = []
    for permutation in itertools.permutations(str(number) for number in numbers):
        result.append(''.join(permutation))
    return max(result)


print(largest_number(input(), input()))
```