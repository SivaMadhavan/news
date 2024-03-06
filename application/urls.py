from django.urls import path, include
from .views import (
    VideoCreateListView, NewsCreateListView,
    VideoDeleteView, NewsDeleteView,
    TrendingListView
)

urlpatterns = [
    path('videos', VideoCreateListView.as_view()),
    path('videos/<int:id>', VideoDeleteView.as_view()),
    path('news', NewsCreateListView.as_view()),
    path('news/<int:id>', NewsDeleteView.as_view()),
    path('trending', TrendingListView.as_view())
]
