from django.urls import path
from ocfl_http import views


urlpatterns = [
        path('', views.root, name='root'),
    ]
