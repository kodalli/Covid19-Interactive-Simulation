from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    data  = []
    return JsonResponse(data, safe=False)