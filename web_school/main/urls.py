from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('access/', AccessListCreateAPIView.as_view(), name='access-list-create'),
    path('access/<int:pk>/', AccessDetailAPIView.as_view(), name='access-detail'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('lesson-watches/', LessonWatchListCreateAPIView.as_view(), name='lesson-watch-list-create'),
    path('lesson-watches/<int:pk>/', LessonWatchDetailAPIView.as_view(), name='lesson-watch-detail'),
    path('lessons-for-product/<int:product_id>/', LessonListWithAccessAPIView.as_view(), name='lesson-list-with-access'),
    path('request-access/', AccessRequestCreateAPIView.as_view(), name='access-request'),
    path('manage-access/', AccessListManageAPIView.as_view(), name='manage-access'),
    path('lessons-for-product/<int:product_id>/', LessonListForProductAPIView.as_view(), name='lesson-for-product'),
    path('product-statistics/', ProductStatisticsAPIView.as_view(), name='product-statistics')
    ]


