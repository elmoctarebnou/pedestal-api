from django.urls import path
from .views import sample_views


urlpatterns = [path("", sample_views.sample_view, name="sample_view_endpoint")]
