from django.urls import path
from . import views
urlpatterns = [
    path("", views.show_topics, name="topics"),
    path("<slug_>", views.show_details, name="topicsdetail")
]