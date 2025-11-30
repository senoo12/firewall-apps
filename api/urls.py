from django.urls import path
from api.api.rule_view import RuleAPI, RuleDetailAPI
from api.api.log_view import LogAPI

urlpatterns = [
    path("rules/", RuleAPI.as_view()),
    path("rules/<uuid:rule_id>/", RuleDetailAPI.as_view()),
    path("logs/", LogAPI.as_view()),
]
