import pytest
import yaml
import json
from crawlers.extension.hybrid_crawler import ExHybridCrawler

@pytest.fixture
def headers():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config['TokenManager']['tiktok']

@pytest.fixture
def hybrid_crawler(headers):
    return ExHybridCrawler(headers)

@pytest.mark.asyncio
@pytest.mark.parametrize('url', [
    'https://www.tiktok.com/@yua_mikami/video/6945369795512552705',
    'https://www.tiktok.com/@yua_mikami/video/7077822368177065218'
])
async def test_hybrid_crawler_parsing_single_video_integration(hybrid_crawler, url):
    """
    Integration test for ExHybridCrawler parsing a single TikKok url
    """
    result = await hybrid_crawler.hybrid_parsing_single_video(url)

    assert result is not None
    assert 'video' in result




