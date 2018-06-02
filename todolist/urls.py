"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from todos.api.resources import getTodoResource
from rest_framework import views, serializers, status
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

get_todo_resource = getTodoResource()
class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()
class EchoView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)

urlpatterns = [
    # path('', include('todos.urls')),
    path('api/', include(getTodoResource().urls)),
    path('jwt/', get_schema_view()),
    path('jwt/auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    path('jwt/auth/token/obtain/', TokenObtainPairView.as_view()),
    path('jwt/auth/token/refresh/', TokenRefreshView.as_view()),
    path('jwt/echo/', EchoView.as_view()),
    path('todos/', include('todos.urls')),
    path('admin/', admin.site.urls),
]
