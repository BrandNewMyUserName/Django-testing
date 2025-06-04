from django.urls import path
from .views import index_view, base_ext, base_view

urlpatterns = [
    path('', index_view),
    path('base/base_ext', base_ext),
    path('base', base_view),
]