from django.urls import path

from .views import RegisterUser, index, LoginUser, logout_user

app_name = 'users'

urlpatterns = [
    path('', index, name="index"),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name="logout"),
]
