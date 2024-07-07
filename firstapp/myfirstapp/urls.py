from django.urls import path
from myfirstapp import views
from myfirstapp import views_api

app_name = 'myfirstapp'
urlpatterns = [
   #punya readStudent
   path('', views.readStudent, name='read-data-student'),
   path('create/', views.createStudent, name='create-data-student'),
   path('update/<str:id>', views.updateStudent, name='update-data-student'),
   path('delete/<str:id>', views.deleteStudent, name='delete-data-student'),

   #Punya readCourse
   path('', views.readCourse, name='read-data-course'),
   path('create/', views.createCourse, name='create-data-course'),
   path('update/', views.updateCourse, name='update-data-course'),
   path('delete/', views.deleteCourse, name='delete-data-course'),

   #path API
   path('api/course',views_api.apiCourse, name='api-view-data-course'),
]