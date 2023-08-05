from kfsd.apps.core.utils.http.base import HTTP
from kfsd.apps.core.utils.http.django.request import DjangoRequest


class APIGateway(HTTP):
    def __init__(self, request=None):
        self.__request = DjangoRequest(request)
        HTTP.__init__(self)

    def getGatewayServiceAPIKey(self):
        return self.getDjangoRequest().findConfigs(["services.api_key"])[0]

    def getDjangoRequest(self):
        return self.__request
