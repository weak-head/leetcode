from typing import List


class TrieNode:
    def __init__(self, data=None, rank=0):
        self.children = {}
        self.rank = rank
        self.data = data
        self.isEnd = False


class AutocompleteSystem1:
    def __init__(self, sentences: List[str], times: List[int]):
        self._root = TrieNode()
        self._keyword = ""
        self._keyword_node = self._root
        for s, d in zip(sentences, times):
            self.addRecord(s, d)

    def addRecord(self, record: str, delta: int):
        """
        """
        node = self._root
        for char in record:
            node = self.addChild(node, char)
        # for sorting we store negative values
        node.rank -= delta

    def addChild(self, parent: TrieNode, char: str) -> TrieNode:
        if char not in parent.children:
            parent.children[char] = TrieNode(char)
        return parent.children[char]

    def leafs(self, node: TrieNode, prefix: str) -> List[str]:

        result = []

        def dfs(node: TrieNode, path: str):
            if not node:
                return

            path += node.data

            if node.rank != 0:
                result.append((node.rank, prefix + path))

            for child in node.children:
                dfs(node.children[child], path)

        dfs(node, "")
        result.sort()
        return map(lambda f: f[1], result[:3])

    def input(self, c: str) -> List[str]:

        if c == "#":
            self._keyword_node.rank -= 1
            self._keyword_node = self._root
            self._keyword = ""
            return []
        else:
            self._keyword += c
            self._keyword_node = self.addChild(self._keyword_node, c)
            return self.leafs(self._keyword_node, self._keyword[:-1])


class AutocompleteSystem2:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.addRecord(sentence, times[i])

    def addRecord(self, sentence, hot):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True
        p.data = sentence
        p.rank -= hot

    def dfs(self, root):
        ret = []
        if root:
            if root.isEnd:
                ret.append((root.rank, root.data))

            for child in root.children:
                ret.extend(self.dfs(root.children[child]))

        return ret

    def search(self, sentence):
        p = self.root
        for c in sentence:
            if c not in p.children:
                return []
            p = p.children[c]
        return self.dfs(p)

    def input(self, c):
        results = []
        if c != "#":
            self.keyword += c
            results = self.search(self.keyword)
        else:
            self.addRecord(self.keyword, 1)
            self.keyword = ""
        return [item[1] for item in sorted(results)[:3]]


class Trie:
    def __init__(self):
        self.node = dict()
        self.words = list()


class AutocompleteSystem3:
    def __init__(self, sentences, times):
        self.trie = Trie()
        self.cache_count = dict()
        self.keyword = ""
        for i, sen in enumerate(sentences):
            self._add_word(sen, self.trie)
            self.cache_count[sen] = times[i]

    def _add_word(self, word, trie):
        for char in word:
            if char not in trie.node:
                trie.node[char] = Trie()
            trie = trie.node[char]
            trie.words.append(word)
        return True

    def _find_words(self, word):
        trie = self.trie
        for char in word:
            if char in trie.node:
                trie = trie.node[char]
            else:
                return []
        return trie.words

    def input(self, c):
        if c != "#":
            self.keyword = self.keyword + c
            words = self._find_words(self.keyword)
            res = []
            for word in words:
                res.append((self.cache_count[word], word))
            res = list(set(res))
            return [s[1] for s in sorted(res, key=lambda x: (-x[0], x[1]))[:3]]
        else:
            self.cache_count[self.keyword] = self.cache_count.get(self.keyword, 0) + 1
            self._add_word(self.keyword, self.trie)
            self.keyword = ""
        return []
