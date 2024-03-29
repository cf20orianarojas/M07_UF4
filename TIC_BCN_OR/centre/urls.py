from django.urls import path
from . import views

urlpatterns = [
    # trucada a les views de templates
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('teachers', views.teachers, name='teachers'),
    path('teacher/<str:pk>/', views.info_teacher, name='teacher'),
    path('student/<str:pk>/', views.info_student, name='student'),
    path('form', views.form, name='form'),
]