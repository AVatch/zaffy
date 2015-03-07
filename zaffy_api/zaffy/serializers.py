from rest_framework import serializers
from zaffy.models import Zaffy


class ZaffySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zaffy
