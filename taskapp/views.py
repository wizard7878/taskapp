from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .serializer import ContentSerializer
from .models import Content, Rate

#custom validation
def _is_my_score_valid(my_score):
    """
    Check if score is between 0 to 5
    """
    if my_score in list(range(0,6)):
        return str(my_score)
    raise serializers.ValidationError('my_score must be between 0 to 5')

# Create your views here.
class ListContentViewSet(viewsets.ViewSet):
    """
    List of contents  
    """
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = ContentSerializer

    def list(self, request, *args, **kwargs):
        """
        GET all contents from database and returns
        """
        contents = Content.objects.all()
        serializer = self.serializer_class(contents, many=True, context = {'request': request})
        return Response(serializer.data)

class CreateRateContentViewSet(viewsets.ViewSet):
    """
    User rating to content. 
    If the content has already been rated, 
    the user rating will be updated
    """
    permission_classes = (IsAuthenticated, )

    def create(self, request, content_id=None, *args, **kwargs):
        content = get_object_or_404(Content, id=content_id)
        rated = Rate.objects.filter(content=content, user=request.user) 
        serializer = ContentSerializer(instance=content, context = {'request': request})
        if str(_is_my_score_valid(request.data.get('my_score'))):
            if rated :
                rated.update(score=request.data.get('my_score'))
                Status = status.HTTP_200_OK
            else:
                Rate.objects.create(user=request.user, content=content, score=request.data['my_score'])
                content.number_of_users_rated += 1
                Status = status.HTTP_201_CREATED
            all_content_score = Rate.objects.filter(content=content).values_list('score', flat=True)
            average = sum(all_content_score) / len(all_content_score)
            content.average_score = average
            content.save()
            return Response(serializer.data, status=Status)

