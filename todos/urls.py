from django.urls import path
from todos.views import TodosAPIView


urlpatterns = [
     path('', TodosAPIView.as_view(), name="todo")
]