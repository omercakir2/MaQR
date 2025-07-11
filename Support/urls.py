from django.urls import path
from . import views


urlpatterns = [
    path('', views.support_view, name='support'),
    path('answer/<int:pk>',views.answer_view,name='answer'),

]