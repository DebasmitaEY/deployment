# urls.py
from django.urls import path
from deploy_app.views import home

urlpatterns = [
    path('', home, name='home'),
]
