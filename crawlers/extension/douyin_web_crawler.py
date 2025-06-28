from crawlers.douyin.web.web_crawler import DouyinWebCrawler


class ExDouyinWebCrawler(DouyinWebCrawler):
    """
    The subclass of DouyinWebCrawler, be able to take headers from outer, others remain the same
    """

    def __init__(self, headers):
        super().__init__()
        self.kwargs = headers

    async def get_douyin_headers(self):
        """
        Simply returns the headers getting from outer
        """
        return self.kwargs
