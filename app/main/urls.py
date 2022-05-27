from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('login/',user_views.LoginView.as_view(template_name='app/login.html'),name='login'),
    path('logout/',user_views.LogoutView.as_view(),name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)