from django.urls import path, include
from snippets import views

from rest_framework.routers import DefaultRouter



#Creating a router and registering our viewsets with it
router = DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)



urlpatterns = [
   path('', include(router.urls)),
 
]
# urlpatterns = format_suffix_patterns(urlpatterns)