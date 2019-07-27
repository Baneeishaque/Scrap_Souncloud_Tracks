from BeautifulSoup import BeautifulSoup, Tag


def get_div_elements_by_class_attribute(beautiful_soup, class_name):
    # type: (BeautifulSoup,str) -> Tag
    return beautiful_soup.findAll('div', attrs={'class': class_name})


def get_first_anchor_element_by_class_attribute(tag, class_name):
    # type: (Tag,str) -> Tag
    return get_first_element_by_class_attribute(tag, 'a', class_name)


def get_first_element_by_class_attribute(tag, element, class_name):
    # type: (Tag,str,str) -> Tag
    return tag.find(element, attrs={'class': class_name})


def get_first_span_element_by_class_attribute(tag, class_name):
    # type: (Tag,str) -> Tag
    return get_first_element_by_class_attribute(tag, 'span', class_name)


def get_first_element_by_custom_attribute(tag, element, attribute_key, attribute_value):
    # type: (Tag,str,str,str) -> Tag
    return tag.find(element, attrs={attribute_key: attribute_value})


def get_first_span_element_by_custom_attribute(tag, attribute_key, attribute_value):
    # type: (Tag,str,str) -> Tag
    return tag.find('span', attrs={attribute_key: attribute_value})
