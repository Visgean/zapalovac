import re
import requests
from pyquery import PyQuery


MAIN_SITE = 'http://www.partezlin.cz/'
JS_CALL_PATTERN = re.compile('odesliSvicku\(this\, (?P<id>\d+)\)\;')


def parse_onclick_function(function_call):
    """
    >>>parse_onclick_function('odesliSvicku(this, 8027);')
    '8027'
    """
    return JS_CALL_PATTERN.match(function_call).groupdict()['id']


def get_list():
    r = requests.get(MAIN_SITE)
    query = PyQuery(r.content)
    parsed = []

    for line in query('table > tr'):
        img_td, content_td, candle_td = line.getchildren()
        name = content_td.getchildren()[0].text
        # burial_details = content_td.getchildren()[1].text
        candle_img = candle_td.find('img')
        flaming = candle_img.attrib['src'] == '../obr/horici.gif'

        if not flaming:
            person_id = parse_onclick_function(candle_img.attrib['onclick'])
        else:
            person_id = None

        parsed.append({
            'name': name,
            'id': person_id,
            'flaming': flaming,
        })
    return parsed


deceased = get_list()
not_flaming = list(
    filter(
        lambda d: not d['flaming'],
        deceased
    )
)

print('{} svíček. {} hoří.'.format(
    len(deceased),
    len(deceased) - len(not_flaming)
))










