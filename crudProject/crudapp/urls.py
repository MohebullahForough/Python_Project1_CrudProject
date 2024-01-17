
from django.urls import path
from . import views

urlpatterns = [
    path('', views.adding, name="homePage"),
    path('editing2/<int:stdId>/', views.editing, name='updatePage'),
    path('deleting2/<int:stdId>/',views.deleting, name='deletingData')
]