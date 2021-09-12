
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [

    path('', views.index,name="index"),
    path('detail/<int:ques_id>/', views.detail,name="detail"),
    path('vote/<int:ques_id>/', views.vote, name="vote"),
    path('results/<int:ques_id>/', views.results, name="results"),
]