from django.urls import include, path, re_path, include
from django.views.generic import RedirectView
from . import views
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),  
    path('home/', views.home, name='home'),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path('userdashboard.html', views.userDashboard, name='userdashboard'),
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
    
    path("aisuggest", views.aiSuggest, name="aisuggest"),
    path('', RedirectView.as_view(url='/pdfupload/')),  # root redirects to pdfupload
    path('pdfupload/', include('pdfupload.urls')),
    path('', RedirectView.as_view(url='/pdfupload/')),   # redirect root
]   # ... your urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



