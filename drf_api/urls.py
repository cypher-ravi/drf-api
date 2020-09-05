
from django.contrib import admin
from django.urls import path,include
from core.views import *

from rest_framework import routers
# from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'groups', GroupViewset)


urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),

    # path('admin/', admin.site.urls),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('',PostView.as_view(),name='test'),
    # path('create/',PostCreateView.as_view(),name='create'),
    # path('api/token/', obtain_auth_token, name='obtain-token')
]
