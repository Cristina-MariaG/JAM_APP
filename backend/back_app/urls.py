from django.urls import path

from back_app.views import views

urlpatterns = [
    # path("", views.index, name="index"),
     path("", views.Collection.as_view()),
]

