# from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from .models import SimData
from .serializers import SimSerializer


class SimViewSet(ModelViewSet):
    queryset = SimData.objects.all()
    serializer_class = SimSerializer

# def index(request):
#     data  = []

#     for item in SimData.objects.all():
#         data.append({
#             'healthyYoung': item.healthyYoung,
#             'healthyYoungFreerider': item.healthyYoungFreerider,
#             'sickYoung': item.sickYoung,
#             'healthyElderly': item.healthyElderly,
#             'healthyElderlyFreerider': item.healthyElderlyFreerider,
#             'sickElderly': item.sickElderly,
#             'vaccines': item.vaccines,
#             'timeSpan': item.timeSpan,
#         })

#     return JsonResponse(data, safe=False)