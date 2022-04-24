from collections import OrderedDict
from rest_framework import serializers

from .models import Content, Rate

class ContentSerializer(serializers.ModelSerializer):
    my_score = serializers.SerializerMethodField()

    def get_my_score(self, obj):
        try:
            my_score = Rate.objects.get(content=obj, user= self.context['request'].user).score
            return my_score
        except:
            return None
            
    class Meta:
        model  =  Content
        fields = ('title', 'average_score', 'my_score' , 'number_of_users_rated')

    def to_representation(self, instance):
        contents = super(ContentSerializer, self).to_representation(instance)
        return OrderedDict([(key, contents[key]) for key in contents if contents[key] is not None])
