from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, decorators, renderers, response, status

from kfsd.apps.endpoints.views.docs.utils import UtilsDoc
from kfsd.apps.endpoints.handlers.utils.arr import ArrHandler
from kfsd.apps.endpoints.handlers.utils.attr import AttrHandler
from kfsd.apps.endpoints.handlers.utils.system import SystemHandler
from kfsd.apps.endpoints.serializers.utils.arr import ArrUtilsInputReqSerializer
from kfsd.apps.endpoints.serializers.utils.attr import AttrUtilsInputReqSerializer
from kfsd.apps.endpoints.serializers.utils.system import SystemInputReqSerializer


class UtilsViewSet(viewsets.ViewSet):
    lookup_field = "identifier"
    lookup_value_regex = '[^/]+'

    def parseInput(self, request, serializer):
        inputSerializer = serializer(data=request.data)
        inputSerializer.is_valid()
        return inputSerializer.data

    def getSystemInputData(self, request):
        return self.parseInput(request, SystemInputReqSerializer)

    def getArrInputData(self, request):
        return self.parseInput(request, ArrUtilsInputReqSerializer)

    def getAttrInputData(self, request):
        return self.parseInput(request, AttrUtilsInputReqSerializer)

    @extend_schema(**UtilsDoc.system_view())
    @decorators.action(detail=False, methods=['post'], renderer_classes=[renderers.JSONRenderer])
    def system(self, request):
        systemHandler = SystemHandler(self.getSystemInputData(request))
        return response.Response(systemHandler.gen(), status.HTTP_200_OK)

    @extend_schema(**UtilsDoc.arr_view())
    @decorators.action(detail=False, methods=['post'], renderer_classes=[renderers.JSONRenderer])
    def arr(self, request):
        arrHandler = ArrHandler(self.getArrInputData(request))
        return response.Response(arrHandler.gen(), status.HTTP_200_OK)

    @extend_schema(**UtilsDoc.attr_view())
    @decorators.action(detail=False, methods=['post'], renderer_classes=[renderers.JSONRenderer])
    def attr(self, request):
        attrHandler = AttrHandler(self.getAttrInputData(request))
        return response.Response(attrHandler.gen(), status.HTTP_200_OK)
