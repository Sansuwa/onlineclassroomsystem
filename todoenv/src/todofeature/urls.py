from django.urls import path, include
from todofeature.views import todo_list_view, todo_add_views, todo_edit_view,todo_delete_view, demo_for_ajax
from rest_framework import routers
from todofeature.viewsets import TaskViewSet



app_name="todofeature"

router = routers.SimpleRouter()
router.register("todo-api",TaskViewSet,basename="tasks")

urlpatterns = [
    path("", todo_list_view, name="todo_list"),  
    path("todo-add/",todo_add_views,name="todo_add"),
    path("todo-edit/<int:taskid>/",todo_edit_view ,name="todo_edit"),
    path("todo-delete/",todo_delete_view ,name="todo_delete"),
    path("demo-for-ajax/",demo_for_ajax ,name="demo_for_ajax"),
    path("api/",include(router.urls)),
        
]


