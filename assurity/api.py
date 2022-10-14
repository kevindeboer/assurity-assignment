
from urllib import request

import requests
from urllib.parse import urljoin
from assurity.config import base_url


class SandboxAPI:

    def get_category_details(self, categoryId):
        url = urljoin(
            base_url,
            '/v1/Categories/{}/Details.json?catalogue=false'.format(categoryId)
        )
        return requests.get(url)
