from django.urls import path
from .views import PostTopListView

app_name = 'post'

urlpatterns = [
    path('', PostTopListView.as_view(),name='post_top'),
]