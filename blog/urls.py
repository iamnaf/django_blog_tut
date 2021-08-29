from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateNew, BlogUpdateView

urlpatterns = [
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateNew.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]