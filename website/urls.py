from django.urls import include, path
from .views import index_view

urlpatterns = [
    path('website', index_view),
]
