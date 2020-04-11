from django.urls import path
from .views import PostTopListView,PostFormView,PostSearchView,PostDetailView

app_name = 'post'

urlpatterns = [
    path('', PostTopListView.as_view(),name='post_top'),
    path('create/',PostFormView.as_view(),name='post_create'),
    path('search/',PostSearchView.as_view(),name='post_search'),
    path('detail/<int:pk>',PostDetailView.as_view(),name='post_detail'),
]