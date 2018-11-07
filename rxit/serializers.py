from rest_framework import serializers
from rxit.models import Prescriber

class PrescriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescriber
        fields = ('id', 'name', 'street', 'city', 'province')