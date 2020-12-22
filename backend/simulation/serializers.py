from rest_framework.serializers import ModelSerializer 
from .models import SimData


class SimSerializer(ModelSerializer):
    class Meta:
        model = SimData
        fields = ['id', 'healthyYoung', 'healthyYoungFreerider', 
        'sickYoung', 'healthyElderly', 'healthyElderlyFreerider', 
        'sickElderly', 'vaccines', 'timeSpan']