from typing import List


def generateParenthesis(n: int) -> List[str]:
    return list(gen_par(n))


permutation_map = {
    0: [],
    1: [[1]]
}

par_map = {
    0: {},
    1: {'()'}
}


def gen_par(n: int) -> List[str]:
    if n in par_map:
        return par_map[n]

    result = set()

    # for all possible permutations of the current n
    # we can generate the parentheses
    for single_permutation in permutations(n):
        partial_results = []

        # for the given permutation compose the parentheses
        # result by aggregating the sub-results
        for number in single_permutation:
            if number == n:
                previous_parens_permutations = gen_par(number - 1)
                for previous_permutation in previous_parens_permutations:
                    result.add('(' + previous_permutation + ')')
            else:
                # collection of all possible parens permutations
                # for the given number
                paren_permutations_for_number = gen_par(number)
                if partial_results == []:
                    partial_results = list(paren_permutations_for_number)
                else:
                    temp_par_result = []
                    for current_result_ix in range(0, len(partial_results)):
                        for number_gen_res in paren_permutations_for_number:
                            temp_par_result.append(
                                partial_results[current_result_ix] + number_gen_res)
                    partial_results = temp_par_result

        # all possible unique results for the given permutation
        for pr in partial_results:
            result.add(pr)

    par_map[n] = result
    return result


def permutations(n):
    '''
    Generate all possible permutations of sums for the the given number.
    E.g. given n = 3 the possible perumations are: [3], [2,1], [1,2], [1,1,1]
    '''
    if n in permutation_map:
        return permutation_map[n]

    result, k = [[n]], (n - 1)

    for k in range(n-1, 0, -1):
        prev_permutations = permutations(n - k)
        for p in prev_permutations:
            result.append([k] + p)

    permutation_map[n] = result
    return result

if __name__ == '__main__':
    print(generateParenthesis(8))
