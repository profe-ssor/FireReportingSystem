from django.urls import path
from firereport.views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(template_name="authentication/passwods/password_reset.html"),
        name="reset_password"
    ),
    path(
        'reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="authentication/passwods/password_reset_sent.html"), 
        name="password_reset_done"
    ),
    path(
        'reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="authentication/passwods/password_reset_form.html"), 
        name="password_reset_confirm"
    ),
    path(
        'reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="authentication/passwods/password_reset_done.html"), 
        name="password_reset_complete"
    ),

    path('', index, name='home'),
    path('reporting/', reporting, name='reporting'),
    path('viewStatus/', viewStatus, name='viewStatus'),
    path('viewStatusDetails/<int:pid>/', viewStatusDetails, name='viewStatusDetails'),
    path('admin_login/', admin_login, name='admin_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('addTeam/', addTeam, name='addTeam'),
    path('manageTeam/', manageTeam, name='manageTeam'),
    path('editTeam/<int:pid>/', editTeam, name='editTeam'),
    path('deleteTeam/<int:pid>/', deleteTeam, name='deleteTeam'),
    path('newRequest/', newRequest, name='newRequest'),
    path('assignRequest/', assignRequest, name='assignRequest'),
    path('teamontheway/', teamontheway, name='teamontheway'),
    path('workinprogress/', workinprogress, name='workinprogress'),
    path('completeRequest/', completeRequest, name='completeRequest'),
    path('allRequest/', allRequest, name='allRequest'),
    path('deleteRequest/<int:pid>/', deleteRequest, name='deleteRequest'),
    path('viewRequestDetails/<int:pid>/', viewRequestDetails, name='viewRequestDetails'),
    path('dateReport/', dateReport, name='dateReport'),
    path('search/', search, name='search'),

    path('changePassword/', changePassword, name='changePassword'),

    path('logout/', Logout, name='logout'),

]
