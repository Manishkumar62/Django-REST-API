from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('student/<int:id>/', views.studentDetailView),

    path('employees/', views.Employees.as_view()),
]