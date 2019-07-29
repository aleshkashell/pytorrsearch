import requests
import logging

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)


class TorrSearch:
    def __init__(self):
        self._session = requests.Session()
        self._init_rutor_variables()

    def _init_rutor_variables(self):
        self._rutor = dict()
        self._rutor['protocols'] = ['http', 'https']
        self._rutor['host'] = ['rutor.is', 'rutor.info', '6tor.net']
        self._rutor['search_string'] = '/search/'
        self._rutor['search_words'] = ''

    def search_rutor(self, search_str):
        for link in self._generate_rutor_links():
            try:
                data = self._session.get(f"{link}{search_str}", allow_redirects=False)
            except requests.exceptions.ConnectionError:
                continue
            _logger.debug(data.status_code)
            _logger.debug(data.headers)
            if data.status_code == 200:
                return data.text
        return None

    def _generate_rutor_links(self):
        links = list()
        for host in self._rutor['host']:
            for proto in self._rutor['protocols']:
                links.append(f"{proto}://{host}{self._rutor['search_string']}")
        return links
