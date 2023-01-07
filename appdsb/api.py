# api.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DSBSerializer
from .models import DSB


@api_view(['GET', 'POST'])
def Dlist(request):
    all_data = DSB.objects.all()
    data = DSBSerializer(all_data, many=True).data
    return Response({'data': data})


class DSBViews(generics.CreateAPIView):
    queryset = DSB.objects.all()
    serializer_class = DSBSerializer
