from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("new", views.new, name="new"),
    path("past", views.past, name="past"),
    path("comments", views.comments, name="comments"),
    path("ask", views.ask, name="ask"),
    path("show", views.show, name="show"),
    path("jobs", views.jobs, name="jobs"),
    path("submit", views.submit, name="submit"),
    path("logreg", views.logreg, name="logreg"),
    path("logout", views.delete_online, name="logout"),
    path("welcome", views.welcome, name="welcome"),
    path("welcome/guidelines", views.guidelines, name="guidelines"),
    path("threads", views.threads, name="threads"),
]