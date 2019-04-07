def longestValidParentheses(s: str) -> int:
    # stack to keep indexes of opened parentheses
    # result map to fill matching parentheses
    st, res_map = [], [0] * len(s)

    for ix, c in enumerate(s):
        if c == '(':
            st.append(ix)
        # c == ')'
        else:
            if len(st) > 0:
                last_op = st.pop()
                res_map[ix] = 1
                res_map[last_op] = 1

    # valid parentheses are represented
    # as the sequence of '1'. the longest sequence
    # corresponds to the longest valid parentheses.
    cur_seq, max_seq = 0, 0
    for c in res_map:
        if c == 0:
            cur_seq = 0
        else:
            cur_seq = cur_seq + 1
            max_seq = max(max_seq, cur_seq)

    return max_seq



if __name__ == '__main__':
    assert longestValidParentheses('') == 0
    assert longestValidParentheses('(()') == 2
    assert longestValidParentheses(')))(((') == 0
    assert longestValidParentheses('()()()') == 6
    assert longestValidParentheses('(()()())') == 8
    assert longestValidParentheses('()())()()()') == 6
    assert longestValidParentheses(')((()))())(())') == 8
    assert longestValidParentheses(')((()))())((((()))))') == 10
    assert longestValidParentheses('()(()') == 2
    assert longestValidParentheses('()((())') == 4
    assert longestValidParentheses('(()(((()') == 2

    print('passed')
