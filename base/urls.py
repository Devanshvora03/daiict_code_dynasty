from django.urls import path
from . import views

urlpatterns = [
    path('lobby/', views.lobby),
    path('studentd/', views.studentd, name='studentd'),

    path('room/', views.room),
    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    # path('register/', views.register, name="register"),
    # path('index/', views.index, name="index"),
    path('', views.register, name="register"),
    path('login',views.login),

]