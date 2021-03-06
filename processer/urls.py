from os import name
from django.urls import path
from. import views


app_name = "processer"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("<int:pk>/", views.Detail.as_view(), name='detail'),
    path("<int:pk>/image/", views.getFrameViaAjax, name="ajax_image"),
]