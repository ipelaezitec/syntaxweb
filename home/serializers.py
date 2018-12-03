from .models import SyntaxPost
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SyntaxPost
        fields = ('content','updated')


