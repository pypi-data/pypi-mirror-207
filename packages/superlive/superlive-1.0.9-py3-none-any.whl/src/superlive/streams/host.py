import requests
from src.superlive.core.http_client import HttpClient


class Host(HttpClient):

    def __init__(self, config):
        super().__init__(config)

        # Create default HTTP client
        self.httpClient = HttpClient(self.config)

    # create Host
    def createHost(self, payload: dict):
        try:
            #print('Host >> createHost is called : %s' % (payload))

            # Create default HTTP client
            httpClient = HttpClient(self.config)

            response = httpClient.sendRequest('POST', 'hosts', payload)

            # response.raise_for_status()
            #data = response.json()
            # if not data['success']: raise Exception(data['error'])

            return response

        except requests.exceptions.HTTPError as error:
            print('HTTPError : %s' % (error))

    # get Hosts
    def getHosts(self, options=None):
        try:
            response = self.httpClient.sendRequest('GET', 'hosts', options)
            return response
        except requests.exceptions.HTTPError as error:
            print('HTTPError : %s' % (error))

    # get Specific Host
    def getHostById(self, hostId: str):
        try:
            response = self.httpClient.sendRequest('GET', f'hosts/{hostId}')
            return response
        except requests.exceptions.HTTPError as error:
            print('HTTPError : %s' % (error))

    # update Host
    def updateHost(self, hostId: str, payload: dict):
        try:
            response = self.httpClient.sendRequest('PUT', f'hosts/{hostId}', payload)
            return response.json()
        except requests.exceptions.HTTPError as error:
            print('HTTPError : %s' % (error))

    # count Host
    def countHost(self):
        try:
            response = self.httpClient.sendRequest('GET', 'hosts/count')
            return response
        except requests.exceptions.HTTPError as error:
            print('HTTPError : %s' % (error))

    # remove Host
    def deleteHostById(self, hostId: str):
        try:
            response = self.httpClient.sendRequest('DELETE', f'hosts/{hostId}')
            return response
        except requests.exceptions.HTTPError as error:
            print('HTTPError : %s' % (error))

