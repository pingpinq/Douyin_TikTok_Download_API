from crawlers.tiktok.app.app_crawler import TikTokAPPCrawler


class ExTikTokAPPCrawler(TikTokAPPCrawler):
    """
    The subclass of TikTokAPPCrawler, be able to take header from outer
    """

    def __init__(self, headers):
        super().__init__()
        self.kwargs = headers

    async def get_tiktok_headers(self):
        """
        Simply returns the headers getting from outer
        """
        return self.kwargs
