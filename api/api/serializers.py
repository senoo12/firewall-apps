from rest_framework import serializers
from api.models.rule import Rule
from api.models.log import FirewallLog

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = "__all__"

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirewallLog
        fields = "__all__"
