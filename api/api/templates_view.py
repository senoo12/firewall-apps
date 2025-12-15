# api/api/templates_view.py
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponseRedirect

class AllowedView(APIView):
    def get(self, request):
        return render(request, "allowed.html")


class BlockedView(APIView):
    def get(self, request):
        return render(request, "blocked.html")


class EntryPointView(APIView):
    def get(self, request):
        # langsung redirect, tidak perlu render
        return HttpResponseRedirect("/allowed/")