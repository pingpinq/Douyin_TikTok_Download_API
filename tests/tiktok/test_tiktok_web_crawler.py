import pytest
import yaml
import json
from crawlers.extension.tiktok_web_crawler import ExTikTokWebCrawler


@pytest.fixture
def headers():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config['TokenManager']['tiktok']

@pytest.fixture
def tiktok_web_crawler(headers):
    return ExTikTokWebCrawler(headers)

@pytest.mark.asyncio
@pytest.mark.parametrize('url, expected_sec_user_id', [
    ('"https://www.tiktok.com/@yua_mikami?lang=ja-JP', 'MS4wLjABAAAA-Rq0N86HaTzt6fKHErvshWxG5mDfLr4hqaQZmnbU7aBRsa59im9welgCBGOmn6pV'),
    ('https://www.tiktok.com/@27_ha84', 'MS4wLjABAAAAg-O3SpJiEflvtkvA0CMHSpMjWu5iCEuAVzqIiFUtxBL-1BVzKwCzbUxPmmENbXXD')
])
async def test_get_sec_user_id_integration(tiktok_web_crawler, url, expected_sec_user_id):
    """
    Integration test getting creator's sec_user_id
    """
    sec_user_id = await tiktok_web_crawler.get_sec_user_id(url)

    assert sec_user_id == expected_sec_user_id

@pytest.mark.asyncio
@pytest.mark.parametrize('sec_uid, cursor, count, cover_format',[
    ('MS4wLjABAAAA-Rq0N86HaTzt6fKHErvshWxG5mDfLr4hqaQZmnbU7aBRsa59im9welgCBGOmn6pV', 0, 35, 2),
    ('MS4wLjABAAAAg-O3SpJiEflvtkvA0CMHSpMjWu5iCEuAVzqIiFUtxBL-1BVzKwCzbUxPmmENbXXD', 0, 35, 2)
])
async def test_fetch_user_posts_integration(tiktok_web_crawler, sec_uid, cursor, count, cover_format):
    """
    Integration test fetching creators' posts list
    """
    posts = await tiktok_web_crawler.fetch_user_post(secUid=sec_uid,
                                                     cursor=cursor,
                                                     count=count,
                                                     coverFormat=cover_format)

    assert posts is not None
    assert 'itemList' in posts