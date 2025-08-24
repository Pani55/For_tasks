from django.urls import path
from task_for_dateformat.views import test_view


urlpatterns = [
    path("test_view/", test_view, name="test_view"),
]
