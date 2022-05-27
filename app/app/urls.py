from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name='home'),
    path('register/',views.registerPage,name='register'),
    path('post/',views.postPage,name='post'),
    path('profile/',views.profilePage,name='profile'),
    path('post/<int:pk>',views.postview.as_view(),name='post-view'),
    path('reg/', views.register),
    path('cal/', views.calculaotrpage,name='cal'),
    path('update/<int:pk>',views.posteditpage,name='post-edit'),
    path('post/<int:id>/delete',views.delete_view,name='delete-post'),
    path('te/',views.test,),

]
