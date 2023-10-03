from django.urls import path,include
from .import views
urlpatterns = [
      path('',views.fun,name='fun'),
      path('addcourse',views.addcourse,name='addcourse'),
      path('addcousedb',views.addcoursedb,name='addcoursedb'),
      path('student', views.student_reg, name='student_reg'),
      path('add_studentdb',views.add_studentdb,name='add_studentdb'),
      path('showstudent',views.showstudent,name='showstudent'),
      path('edit/<int:pk>',views.edit,name='edit'),
      path('editdb/<int:pk>',views.editdb,name='editdb'),
      path('delete/<int:pk>',views.delete,name='delete'),

]