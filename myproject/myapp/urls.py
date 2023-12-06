# myapp/urls.py

from django.urls import path
from .views import StudentListCreateView, StudentDetailView, RatingListCreateView, RatingDetailView
from .views import all_data

urlpatterns = [
    path('api/students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('api/students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('api/ratings/', RatingListCreateView.as_view(), name='rating-list-create'),
    path('api/ratings/<int:pk>/', RatingDetailView.as_view(), name='rating-detail'),
    path('all-data/', all_data, name='all_data'),
]





