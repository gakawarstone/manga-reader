import logging
import os
from pprint import pprint
from urllib.request import Request, urlopen, urlretrieve

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class MangaSource:
    url = 'https://read.yagami.me/'


class Manga:
    name = ''


class Chapter:
    num = 1


def get_webpage():
    manga_name = 'yuukoku_no_moriarty'
    volume_num = 11
    chapter_num = 43

    for page_num in range(1, 50):
        url = f'https://read.yagami.me/read/{manga_name}/{volume_num}/{chapter_num}/page/{page_num}'

        logger.info('Visiting url: ' + url)
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=headers)
        resp = urlopen(req).read()
        soup = BeautifulSoup(resp, 'html.parser')
        img_url = soup.select_one('#miku')['src']

        if str(chapter_num) not in os.listdir('./src'):
            logger.debug(f'List dirs: ' + str(os.listdir('./src')))
            logger.info(f'Making directory for chapter {chapter_num}')
            os.mkdir(f'src/{chapter_num}')

        logger.info('Download img from: ' + img_url)
        urlretrieve(img_url, f'src/{chapter_num}/{page_num}.jpg')
        logger.info('Download complete')


if __name__ == '__main__':
    get_webpage()
