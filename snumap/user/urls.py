from django.urls import path
from .views import UserSignUpView, UserLoginView, UserLogoutView

urlpatterns = [
    path('signup', UserSignUpView.as_view(), name='signup'),    # /signup
    path('login', UserLoginView.as_view(), name='login'),       # /login
    path('logout', UserLogoutView.as_view(), name='logout'),    # /logout
]