from django.http import JsonResponse
from django.shortcuts import render


#third party imports
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

#importing serializers
from .serializers import PostSerializer
from .models import Post


class PostView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
   

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        # fields = ('title', 'description', 'owner')
        # serializer = PostSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors)
        return self.create(request, *args, **kwargs)



# class TestView(APIView):
#     permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         searializer = PostSerializer(qs, many=True)
#         return Response(searializer.data)

#     def post(self, request, *args , **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

class PostCreateView(mixins.ListModelMixin,generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    