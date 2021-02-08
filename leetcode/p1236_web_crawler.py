from urllib.parse import urlparse
from typing import List


class HtmlParser:
    def __init__(self, m):
        self.m = m

    def getUrls(self, url):
        return self.m[url]


def crawl(startUrl: str, htmlParser: "HtmlParser") -> List[str]:
    """
    Time: O(n)
    Space: O(n)
        n - number of reachable links under the root domain
    """

    def get_domain(link):
        return urlparse(link).netloc

    def get_domain2(link):
        t = link.split("http://")[1]
        domain = t.split("/")[0]
        return domain

    def dfs(link, links, root):
        if link in links:
            return

        if get_domain(link) != root:
            return

        links.add(link)
        for l in htmlParser.getUrls(link):
            dfs(l, links, root)

    links = set()
    dfs(startUrl, links, get_domain(startUrl))
    return links
