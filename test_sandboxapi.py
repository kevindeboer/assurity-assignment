import json
import pytest
from assurity.api import SandboxAPI


@pytest.fixture()
def sandbox_api():
    yield SandboxAPI()

def test_get_category_details(sandbox_api):
    response = sandbox_api.get_category_details(6327)
    assert(response.status_code == 200)
    
    response_content = json.loads(response.content)
    assert(response_content.get('Name') == 'Carbon credits')
    assert(response_content.get('CanRelist'))
    promotion = next(p for p in response_content.get('Promotions') if p.get('Name') == 'Gallery')
    assert("Good position in category" in promotion.get('Description'))


