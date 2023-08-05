from kfsd.apps.core.exceptions.api import KubefacetsAPIException
from kfsd.apps.core.utils.http.headers.cookie import Cookie
from kfsd.apps.core.utils.dict import DictUtils


class Response(Cookie):
    def __init__(self):
        self.__response = None

    def getResponse(self):
        return self.__response

    def setResponse(self, response):
        self.__response = response
        self.setCookiesHttpObj(response)

    def getStatusCode(self):
        return self.__response.status_code

    def raiseAPIException(self):
        resp = self.getResponse().json()
        errorStr = DictUtils.get(resp, "detail", "Unknown error detail")
        errorCode = DictUtils.get(resp, "code", "unexpected_error")
        raise KubefacetsAPIException(errorStr, errorCode, self.getStatusCode())

    def isRespValid(self, expStatusCode):
        if isinstance(expStatusCode, int) and not expStatusCode == self.getStatusCode():
            self.raiseAPIException()

        if (
            isinstance(expStatusCode, list)
            and self.getStatusCode() not in expStatusCode
        ):
            self.raiseAPIException()

        return True
