from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name= 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<slug:slug>/', views.ProfileView.as_view(), name='profile'),
    path('profile/update/<slug:slug>/', views.UpdateProfileView.as_view(), name='update'),
    path('profile/delete/<slug:slug>/', views.DeleteProfileView.as_view(), name='delete'),
]
