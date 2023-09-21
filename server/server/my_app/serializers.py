

from .models import MyModal
from rest_framework import serializers


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModal
        fields = ('id', 'name')
