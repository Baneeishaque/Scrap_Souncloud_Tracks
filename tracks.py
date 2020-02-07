from typing import List, Any, Union

from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from beautifulSoupUtils import get_div_elements_by_class_attribute
from beautifulSoupUtils import get_first_anchor_element_by_class_attribute

# from beautifulSoupUtils import get_first_span_element_by_custom_attribute
# from cssutilsHelpers import get_backgroundImage_url

chromeWebDriver = webdriver.Chrome("C:/Programs/chromedriver.exe")  # type: WebDriver

chromeWebDriver.get("https://soundcloud.com/search/sounds?q=old%20party")
pageSource = chromeWebDriver.page_source  # type: Union[Union[int, List[Union[int, str]]], Any]
beautifulSoapContent = BeautifulSoup(pageSource)  # type: BeautifulSoup

for soundBody in get_div_elements_by_class_attribute(beautifulSoapContent, 'sound__body'):  # type: Tag

    # print "sound__body Element : " + str(soundBody) + "\n"

    coverArtElement = get_first_anchor_element_by_class_attribute(soundBody, 'sound__coverArt')  # type: Tag
    # print "sound__coverArt Element : " + str(coverArtElement)

    trackPage = "https://soundcloud.com" + coverArtElement.get('href')  # type: Union[Union[str, unicode], Any]
    print("Track Page : " + trackPage)

    # TODO : Wait to load Cover Arts
    # coverArtUrl = get_backgroundImage_url(
    #     get_first_span_element_by_custom_attribute(coverArtElement, 'aria-role', 'img'))  # type: str
    # print "Cover Art Url : " + coverArtUrl

    contentElement = get_first_anchor_element_by_class_attribute(soundBody, 'sound__content')  # type: Tag
    # print "sound__content Element : " + str(contentElement)
