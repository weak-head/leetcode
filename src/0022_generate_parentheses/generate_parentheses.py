from typing import List

def generateParenthesis(n: int) -> List[str]:
    res = gen_par(n)
    results = []
    for r in res:
        results.append(''.join(r))
    return list(set(results))

def gen_par(n: int) -> List[List[str]]:
    if n <= 0:
        return []
    if n == 1:
        return [['()']]

    sub_results = gen_par(n - 1)
    results = []
    for s_res in sub_results:
        results.append(['()'] + s_res)
        results.append(s_res + ['()'])
        results.append(['('] + s_res + [')'])
        for ix, child_res in enumerate(s_res):
            if child_res == '()':
                results.append(s_res[:ix] + ['(', '()', ')'] + s_res[ix+1:])
            elif child_res == '(':
                # find matching parenthes
                ix_r, cnt = ix + 1, 0
                while s_res[ix_r] != ')' and cnt == 0:
                    if s_res[ix_r] == '(':
                        cnt = cnt + 1
                    if s_res[ix_r] == ')':
                        cnt = cnt - 1
                    ix_r = ix_r + 1
                results.append(s_res[:ix] + ['('] + s_res[ix:ix_r + 1] + [')'] + s_res[ix_r + 1:])
    return results


if __name__ == '__main__':
    print(generateParenthesis(4))