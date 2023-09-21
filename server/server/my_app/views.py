from django.shortcuts import render



from .models import MyModal
from .serializers import MyModelSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def nameAPI(request):
    queryset = MyModal.objects.all()
    serializer_class = MyModelSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False)


@api_view(['POST'])
def add_new_name(request):
    # add new name
    name = request.data.get('name')
    new_name = MyModal.objects.create(name=name)
    
    # return all names
    queryset = MyModal.objects.all()
    serializer_class = MyModelSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False)