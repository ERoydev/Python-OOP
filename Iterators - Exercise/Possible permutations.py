

def possible_permutations(numbers):
    if len(numbers) <= 1:
        yield numbers

    else:
        for i in range(len(numbers)):
            for perm in possible_permutations(numbers[:i] + numbers[i + 1:]):
                yield [numbers[i]] + perm



[print(n) for n in possible_permutations([1, 2, 3])]