import json
import requests

from watch_together import settings


def get_master_manifest(content_id):
    cms_url = 'https://cmsosiris.hotstar-labs.com/clip/contentId/' + \
              str(content_id)
    cms_token = settings.CMS_TOKEN
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': cms_token,
        'x-tenant-id': "in",
    }
    response = requests.get(cms_url, headers=headers)
    response_dict = json.loads(response.text)
    return response_dict['body']['results']['platformData'][0]['playbackUrl']

