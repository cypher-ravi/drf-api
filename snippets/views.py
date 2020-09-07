from django.shortcuts import render
from django.http import Http404


#status module and Response object instead of JSONresponse, added permission,adding apiview decorator for simple api root
from rest_framework import status
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers



#mixins and generic views for class based views
from rest_framework import mixins
from rest_framework import generics
#using viewsets
from rest_framework import viewsets



#models and Snippet Serializer
from snippets.serializers import SnippetSerializer,UserSerializer
from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly



#functional based view to entering into our api
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users':reverse('user-list', request=request, format=format),
        'snippets':reverse('snippet-list', request=request, format=format),

    })


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

# Create API view using class based views.
class SnippetList(generics.ListCreateAPIView):
    """

    List all code snippets and create snippet

    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve update and delete a code snippet.

    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]




class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, update and destroy actions.

    Additionally we also added extra highlight action 

    """
  
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)

#Refractoring into viewsets
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """

    this viewset automatically provides `list` and `details` action

    """

    queryset = User.objects.all()
    serializer_class = UserSerializer