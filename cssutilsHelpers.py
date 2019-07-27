import cssutils
from BeautifulSoup import Tag


def get_backgroundImage_url(tag):
    # type: (Tag) -> str
    return cssutils.parseStyle(tag.get('style')).backgroundImage.replace('url(', '').replace(')', '')
