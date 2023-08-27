from django.urls import path
from . import views

urlpatterns = [
    path('lobby/', views.lobby),
    path('room/', views.room),

    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),

    path('studentd/', views.studentd, name='studentd'),
    path('facultyd/', views.studentd, name='facultyd'),

    path('', views.register, name="register"),
    path('login/',views.login),
    path('schedule/',views.schedule),
]