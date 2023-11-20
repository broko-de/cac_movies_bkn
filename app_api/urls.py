from django.urls import path, re_path, include
from . import views



from django.contrib.auth import views as auth_views


urlpatterns = [
    path('movies/', views.movies_list),
    path('movies/<int:pk>/', views.movies_detail),
    
    path('api-auth/', include('rest_framework.urls'))
]