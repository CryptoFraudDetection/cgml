"""
This module contains the tests for the scraper.comparitech module.
"""

import CryptoFraudDetection.utils.logger as logger
from CryptoFraudDetection.scraper.reddit import RedditScraper
from CryptoFraudDetection.utils.enums import LoggerMode
import json

logger_ = logger.Logger(name=__name__, level=LoggerMode.DEBUG, log_dir="../logs")


def test_initialization():
    """
    Test the initialization of the RedditScraper class
    """
    scraper = RedditScraper(logger_, '', '', '')
    scraper.quit()


def test__extract_all_comments():
    """
    Test the _extract_comments method of the RedditScraper class
    """
    scraper = RedditScraper(logger_, '', '', '')
    url = 'https://old.reddit.com/r/Fire/comments/11lfj4e/lost_400000_my_whole_net_worth_to_the_terra_luna/'
    scraper.scrape_post_content(url)
    comments = scraper._extract_all_comments()
    with open('comments.json', 'w') as f:
        json.dump(comments, f)


def test_scrape_post_content():
    """
    Test the scrape_post_content method of the RedditScraper class
    """
    scraper = RedditScraper(logger_, '', '', '')
    url = 'https://old.reddit.com/r/Fire/comments/11lfj4e/lost_400000_my_whole_net_worth_to_the_terra_luna/'
    post = scraper.scrape_post_content(url)

    assert post.get('text', None) not in [None, '']
    #assert isinstance(post.get('score', None), int)
    
    # # Check if the first comment has the required keys
    # for key in ['id', 'author', 'text', 'score', 'date', 'children']:
    #     assert post['children'][0].get(key, None)
    # # Check if the first child of the first comment has the required keys
    # for key in ['id', 'author', 'text', 'score', 'date', 'children']:
    #     assert post['children'][0]['children'][0].get(key, None)
    scraper.quit()
    
if __name__ == '__main__':
    test__extract_all_comments()
    