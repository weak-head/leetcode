from collections import Counter, defaultdict


class FreqStack:
    """
    Frequency Stack that is based on two dictionaries:
        - one keeps frequencies of elements
        - another keep groups of elements based on frequencies
    """

    def __init__(self):
        """
        Freq and Group dictionaries

        Space: O(n)
            n - number of elements in the stack
        """
        # frequency of each unique element
        self.freq = Counter()
        # groups of frequencies
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        """
        Time: O(1)
        """
        # increase the frequency of the element
        self.freq[x] += 1

        # keep max
        self.maxfreq = max(self.maxfreq, self.freq[x])

        # group by frequency and preserve order
        self.group[self.freq[x]].append(x)

    def pop(self):
        """
        Time: O(1)
        """
        # extract max frequency
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1

        # decrease max if required
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x
