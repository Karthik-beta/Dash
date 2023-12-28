from rest_framework import serializers
from . import models

class MaterialTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaterialTransaction
        fields = '__all__'