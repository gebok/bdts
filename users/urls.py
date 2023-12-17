from django.urls import path
from .views import home, RegisterView, motto

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('motto/', motto, name='users-motto'),
]