from crawlers.tiktok.web.web_crawler import TikTokWebCrawler


class ExTikTokWebCrawler(TikTokWebCrawler):
    """
    The subclass of TikTokWebCrawler, able to take the headers from out of the class, others remain the same
    """

    def __init__(self, headers):
        super().__init__()
        self.kwargs = headers

    async def get_tiktok_headers(self):
        """
        Simply returns the headers getting from outer
        """
        return self.kwargs
