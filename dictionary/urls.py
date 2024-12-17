from django.urls import path

from . import views

app_name = "dictionary"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("TS-EL/<str:entry>", views.tsakonian, name="tsakonian"),
    path("EL-TS/<str:entry>", views.greek, name="greek"),
    path("writing_extension/", views.writing_extension, name="writing_extension"),
    path("preservation_strategy/", views.preservation_strategy, name="preservation_strategy"),
    path("chat/", views.chat, name="chat"),
]