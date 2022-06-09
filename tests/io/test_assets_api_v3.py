'''
Test Findings -> Assets V3 API endpoints
'''
import pytest
from requests import Response

from tenable.io.v3.base.iterators.explore_iterator import CSVChunkIterator, SearchIterator

BASE_URL = 'https://cloud.tenable.com/api/v3'
ASSET_BASE_URL = f'{BASE_URL}/assets'


@pytest.mark.vcr()
def test_findings_assets_v3_search_was_assets(api):
    '''
    Test the search web applications assets endpoint
    '''
    fields = ['name', 'id', 'last_observed', 'tags']
    sort = [('created', 'desc')]
    filters = ('and', ('last_observed', 'lt', '2022-04-19T18:30:00.000Z'),
               ('tags', 'eq', ['6167eae5-808a-415a-8400-f3208e5382c5']))

    iterator = api.v3.explore.assets.search_webapp(
        fields=fields, limit=200, sort=sort, filter=filters
    )
    assert isinstance(iterator, SearchIterator), \
        "Iterator is not returned in response of Findings -> Web Applications Assets"

    iterator = api.v3.explore.assets.search_webapp(
        fields=fields, return_csv=True, sort=sort, limit=200, filter=filters
    )
    assert isinstance(iterator, CSVChunkIterator), "CSV chunk iterator is not returned in response of " \
                                                   "Findings -> Web Applications Assets with return_csv flag enabled"

    resp = api.v3.explore.assets.search_webapp(
        fields=fields, return_resp=True, limit=200, sort=sort,
        filter=filters)
    assert isinstance(resp, Response), "Response is not returned in response of " \
                                       "Findings -> Web Applications Assets with return_resp flag enabled"