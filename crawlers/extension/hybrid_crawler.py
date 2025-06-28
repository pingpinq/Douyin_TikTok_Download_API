from crawlers.hybrid.hybrid_crawler import HybridCrawler
from crawlers.extension.douyin_web_crawler import ExDouyinWebCrawler
from crawlers.extension.tiktok_web_crawler import ExTikTokWebCrawler
from crawlers.extension.tiktok_app_crawler import ExTikTokAPPCrawler

class ExHybridCrawler(HybridCrawler):
    """
    The subclass of HybridCrawler, be able to take the header from outer
    """

    def __init__(self, header):
        super().__init__()
        self.DouyinWebCrawler = ExDouyinWebCrawler(header)
        self.TikTokWebCrawler = ExTikTokWebCrawler(header)
        self.TikTokAPPCrawler = ExTikTokAPPCrawler(header)
