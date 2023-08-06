import string
from itertools import chain

# style properties to duplicate
# can't use shorthand properties:
#     `getCssValue` in: https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/WebElement.html
# not inherited: background-color, display, margin, padding
TARGET_CSS_PROPS = ('color', 'white-space', 'font-weight', 'font-style', 'font-size',
                    'padding-top', 'padding-right', 'padding-bottom', 'padding-left',
                    'margin-top', 'margin-right', 'margin-bottom', 'margin-left',
                    'background-color', 'display')



# non-inheritable property names and their default computed values
DEFAULT_NOINHERIT_PROP_MAP = {
    'background-color': 'rgba(0, 0, 0, 0)',
    'padding-top': '0px',
    'padding-right': '0px',
    'padding-bottom': '0px',
    'padding-left': '0px',
    'margin-top': '0px',
    'margin-right': '0px',
    'margin-bottom': '0px',
    'margin-left': '0px',
    'display': 'inline'
}


RAND_ID_CHARSPACE = tuple(chain.from_iterable((string.ascii_letters, string.digits)))
RAND_ID_LEN = 8


HTML_ELEMENT_FMT_STR = '<{} id="{}">{}</{}>'
HTML_DOCUMENT_FMT_STR = '<!DOCTYPE html>\n<html>\n\t<head>{}</head>\n\t<body>\n\t{}\n\t</body>\n</html>'
CSS_HREF_FMT_STR = '<link rel="stylesheet" type="text/css" href="{}">'


INNER_HTML_SELECTOR = 'innerHTML'
OUTER_HTML_SELECTOR = 'outerHTML'


CSS_DECLARATION_FMT_STR = '\t{}: {};'
CSS_RULESET_FMT_STR = '{} {{\n{}\n}}'


CODE_XPATH_SELECTOR = '//*/code'
PARENT_REL_XPATH_SELECTOR = './..'
