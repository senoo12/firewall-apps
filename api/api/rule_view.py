from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.api.serializers import RuleSerializer
from api.repositories.rule_repo import RuleRepository


class RuleAPI(APIView):

    def get(self, request):
        """Ambil semua rules"""
        rules = RuleRepository.get_all()
        serializer = RuleSerializer(rules, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Tambah rule baru"""
        serializer = RuleSerializer(data=request.data)
        if serializer.is_valid():
            rule = RuleRepository.create(serializer.validated_data)
            return Response(RuleSerializer(rule).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RuleDetailAPI(APIView):

    def get(self, request, rule_id):
        """Ambil rule berdasarkan ID"""
        rule = RuleRepository.get_by_id(rule_id)
        if not rule:
            return Response({"detail": "Rule not found"}, status=404)

        return Response(RuleSerializer(rule).data)

    def delete(self, request, rule_id):
        """Hapus rule"""
        rule = RuleRepository.get_by_id(rule_id)
        if not rule:
            return Response({"detail": "Rule not found"}, status=404)

        RuleRepository.delete(rule_id)
        return Response({"message": "Rule deleted"}, status=200)
