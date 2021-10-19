from django.urls import path
from . import views

urlpatterns = [
    path('projectForm/',views.projectForm,name="projectForm"),
    path('',views.showlist,name="showlist"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    
]
