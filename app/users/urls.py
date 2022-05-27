from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('profile/',views.userpage,name='profile'),
    path('post/<int:pk>',views.viewDetail.as_view(),name='Postview')
]
