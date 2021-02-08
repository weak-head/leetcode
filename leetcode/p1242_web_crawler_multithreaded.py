from typing import List
from collections import deque
from concurrent import futures


class HtmlParser:
    def __init__(self, m):
        self.m = m

    def getUrls(self, url):
        return self.m[url]


def crawl(startUrl: str, htmlParser: "HtmlParser") -> List[str]:
    """
    BFS using queue and worker pool.

    Create worker pool and assign workers to processes the urls.
    One worker processes one url.
    Main thread collects results from each worker and schedules a new workers if reqired.

    Time: O(n)
    Space: O(n)
        n - number of reachable links under root domain.
    """

    def hostname(url):
        return url.split("/")[2]

    root = hostname(startUrl)
    seen = {startUrl}
    with futures.ThreadPoolExecutor(max_workers=16) as executor:
        tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
        while tasks:

            # urls retrived by some worker
            urls = tasks.popleft().result()  # blocks
            for url in urls:
                if url not in seen and hostname(url) == root:
                    seen.add(url)
                    tasks.append(executor.submit(htmlParser.getUrls, url))
    return seen
