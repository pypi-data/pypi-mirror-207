from django.urls import path

from . import views

urlpatterns = [
    path("num_one/", views.start_quiz, name="num_one_quiz")
]