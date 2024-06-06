# made by me---sonam

from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("python", views.python, name="python"),
    path("py1", views.py1, name="py1"),
    path("py2", views.py2, name="py2"),
    path("py3", views.py3, name="py3"),
    path("django", views.django, name="django"),
    path("dj1", views.dj1, name="dj1"),
    path("dj2", views.dj2, name="dj2"),
    path("dj3", views.dj3, name="dj3"),
    path("cpp", views.cpp, name="cpp"),
    path("cpp1", views.cpp1, name="cpp1"),
    path("cpp2", views.cpp2, name="cpp2"),
    path("cpp3", views.cpp3, name="cpp3"),
    path("news", views.news, name="news"),
    path("rules", views.rules, name="rules"),
    path("result", views.result, name="result"),
    path("questions", views.question_list, name="question_list"),



]
