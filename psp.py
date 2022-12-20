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
