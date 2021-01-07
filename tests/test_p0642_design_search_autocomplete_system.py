from leetcode.p0642_design_search_autocomplete_system import (
    AutocompleteSystem1,
    AutocompleteSystem2,
    AutocompleteSystem3,
)


def test_trie():
    sentences = ["i love you", "island", "iroman", "i love leetcode"]
    times = [5, 3, 2, 2]
    systems = [AutocompleteSystem1, AutocompleteSystem2, AutocompleteSystem3]

    for sc in systems:
        s = sc(sentences, times)
        assert list(s.input("i")) == ["i love you", "island", "i love leetcode"]
        assert list(s.input(" ")) == ["i love you", "i love leetcode"]
        assert list(s.input("a")) == []
        assert list(s.input("#")) == []
