from django.contrib import admin
from django.urls import path, include

from e_commerce import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='home'),
    path('user/', include('users.urls', namespace='users'))
]
