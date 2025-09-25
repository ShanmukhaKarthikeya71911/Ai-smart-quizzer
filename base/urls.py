from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),  
    path('home/', views.home, name='home'),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("register", views.register, name="register"),
    path("quiz/<str:pk>/", views.quiz, name="quiz"),
    path("result", views.result, name="result"),
    path("profile", views.profile, name="profile"),
    path("admin", views.adminPage, name="admin"),
    path("admindashboard", views.adminDashboard, name="admindashboard"),
    path("add-quiz", views.addQuiz, name="add-quiz"),
    path("contactus", views.contactus, name="contactus"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("updatequiz/<str:pk>/", views.updateQuiz, name="updatequiz"),
    path("deletequiz/<str:pk>/", views.deleteQuiz, name="deletequiz"),
    path("addquestion", views.addQuestion, name="addquestion"),
    path("userdashboard", views.userDashboard, name="userdashboard"),
    path("aisuggest", views.aiSuggest, name="aisuggest"),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
