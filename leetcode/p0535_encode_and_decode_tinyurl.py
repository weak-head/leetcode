class Codec:
    """
    Very simplified version of hashing URLs.
    """

    def __init__(self):
        self.m = {}

    def encode(self, longUrl: str) -> str:
        h = str(hash(longUrl))
        self.m[h] = longUrl
        return f"http://tinyurl.com/{h}"

    def decode(self, shortUrl: str) -> str:
        h = shortUrl.replace("http://tinyurl.com/", "")
        return self.m[h]
