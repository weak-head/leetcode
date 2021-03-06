from typing import List

# ----------------------------------------------------
# -- Using Dynamic Programming and number allocation permutations
# -- hard to follow


def generateParenthesis(n: int) -> List[str]:
    return list(gen_par(n))


permutation_map = {0: [], 1: [[1]]}

par_map = {0: {}, 1: {"()"}}


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
                    result.add("(" + previous_permutation + ")")
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
                                partial_results[current_result_ix] + number_gen_res
                            )
                    partial_results = temp_par_result

        # all possible unique results for the given permutation
        for pr in partial_results:
            result.add(pr)

    par_map[n] = result
    return result


def permutations(n):
    """
    Generate all possible permutations of sums for the the given number.
    E.g. given n = 3 the possible perumations are: [3], [2,1], [1,2], [1,1,1]
    """
    if n in permutation_map:
        return permutation_map[n]

    result, k = [[n]], (n - 1)

    for k in range(n - 1, 0, -1):
        prev_permutations = permutations(n - k)
        for p in prev_permutations:
            result.append([k] + p)

    permutation_map[n] = result
    return result


# --------------------------------------------------
# -- Using backtracking


def generateParenthesis2(n: int) -> List[str]:
    result = []
    gen_par_back("", n, 0, 0, result)
    return result


def gen_par_back(s: str, n: int, op: int, cp: int, result: List[str]) -> None:
    # we have exhausted all possible combinations
    if cp == n:
        return

    # we have exhausted all possible combinations for opened pars
    if op == n:
        result.append(s + (")" * (n - cp)))
        return

    # op < n
    gen_par_back(s + "(", n, op + 1, cp, result)

    if op > cp:
        gen_par_back(s + ")", n, op, cp + 1, result)


# --------------------------------------------------
# -- Using backtracking (easier to follow)


def generateParenthesis4(n: int) -> List[str]:
    if n == 0:
        return []

    result = []

    def backtrack(s, opened_par, closed_par, n, result):
        if closed_par == n:
            result.append(s)
            return

        if opened_par < n:
            backtrack(s + "(", opened_par + 1, closed_par, n, result)

        if opened_par > closed_par and closed_par < n:
            backtrack(s + ")", opened_par, closed_par + 1, n, result)

    backtrack("", 0, 0, n, result)
    return result


# ----------------------------------------------------
# -- Using Dynamic Programming (easy to follow)


def generateParenthesis3(n: int) -> List[str]:
    pars = {0: set(), 1: {"()"}}

    def gen_par_dyn(n):
        if n in pars:
            return pars[n]

        res = set()
        for k in range(1, n):
            res.update([lp + rp for lp in gen_par_dyn(n - k) for rp in gen_par_dyn(k)])

        for par_per in gen_par_dyn(n - 1):
            res.add("(" + par_per + ")")

        pars[n] = res
        return res

    return gen_par_dyn(n)
