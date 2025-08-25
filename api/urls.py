from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employees')

urlpatterns = [
    path('students/', views.studentsView),
    path('student/<int:id>/', views.studentDetailView),

    # path('employees/', views.Employees.as_view()),
    # path ('employees/<int:id>/', views.EmployeeDetail.as_view()),

    path('', include(router.urls)),
]