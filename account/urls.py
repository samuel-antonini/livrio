from django.urls import path

from account import views

urlpatterns = [
    path('register/', views.register, name="account-register"),
    path('activate/', views.activate_account, name="account-activate"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

]
