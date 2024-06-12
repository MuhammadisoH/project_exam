from django.urls import path 
from . import views


urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('kirimlar/', views.kirimlar_view, name='kirimlar'),
    path('kirimlar/delete/<int:id>/', views.delete_kirim_view, name='delete_kirim'),
    path('chiqimlar/', views.chiqimlar_view, name='chiqimlar'),
    path('hisobotlar/', views.hisobotlar_view, name='hisobotlar'),
]