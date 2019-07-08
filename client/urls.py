from django.urls import path
from django.conf.urls import url
from client import views

urlpatterns = [
    path('', views.client, name='client'),
    path('delete/<int:pk>', views.ClientDelete.as_view(success_url="/"),
         name='client_delete'),
]
