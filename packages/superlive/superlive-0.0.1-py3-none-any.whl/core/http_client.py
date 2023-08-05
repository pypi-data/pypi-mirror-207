import requests
import json

class HttpClient:

    def __init__(self, config: None):
        self.config = {
            'api_endpoint': config.get('api_endpoint') or '',
            'api_key': config.get('api_key') or '',
        }

    def sendRequest(self, method: str, endpoint: str, payload={}):
        try:
            # Add the Authorization header
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'text/plain',
                'Authorization': self.config["api_key"]
            }

            response = requests.request(method=method, url=f'{self.config["api_endpoint"]}/{endpoint}', data=json.dumps(payload), headers=headers)
            #print('HttpClient TYPE : %s' % (type(response)))
            print('HttpClient response : %s' % (response.content))
            return response.json()

        except requests.exceptions.HTTPError as error:
            print('HTTPError : %s' %(error.response))