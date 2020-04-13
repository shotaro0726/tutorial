from django.urls import path
from .views import PostTopListView,PostCreateFormView,PostSearchView,PostDetailView,PostClaimView,PostUpdateView,PostDeleteView

app_name = 'post'

urlpatterns = [
    path('', PostTopListView.as_view(),name='post_top'),
    path('create/',PostCreateFormView.as_view(),name='post_create'),
    path('search/',PostSearchView.as_view(),name='post_search'),
    path('detail/<int:pk>',PostDetailView.as_view(),name='post_detail'),
    path('claim/',PostClaimView.as_view(),name='post_claim'),
    path('update/<int:pk>',PostUpdateView.as_view(),name='post_update'),
    path('delete/<int:pk>',PostDeleteView.as_view(),name='post_delete'),
]