from django.urls import path
from .import views

urlpatterns = [

    path('todo/',views.todoView,name='todo'),
    path('addtodo/',views.addtodo),
    path('deletetodo/<int:todo_id>/',views.deletetodo,name='delete')
]
