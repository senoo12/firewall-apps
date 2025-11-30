from rest_framework.views import APIView
from rest_framework.response import Response

from api.models.log import FirewallLog
from api.api.serializers import LogSerializer


class LogAPI(APIView):

    def get(self, request):
        """Ambil seluruh log firewall"""
        logs = FirewallLog.objects.all().order_by("-timestamp")
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)