from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
import random

from .forms import RegisterForm, LoginForm
from .models import Quiz, Question, Result  # remove CustomUser if unused

# base/views.py
from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def home(request):
    quizzes = Quiz.objects.all()
    return render(request, "home.html", {"quizzes": quizzes})

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, "register.html", {"form": form})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, "register.html", {"form": form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html", {"form": form})


@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")


@login_required(login_url="login")
def quiz(request, pk):
    quiz = Quiz.objects.get(id=pk)
    questions = list(Question.objects.filter(quiz=quiz))
    random.shuffle(questions)
    if request.method == "POST":
        score = 0
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            if selected_option == question.correct_option:
                score += 1
        Result.objects.create(user=request.user, quiz=quiz, score=score)
        return redirect("result")
    return render(request, "quiz.html", {"quiz": quiz, "questions": questions})


@login_required(login_url="login")
def result(request):
    results = Result.objects.filter(user=request.user).order_by('-date_taken')
    return render(request, "result.html", {"results": results})


@login_required(login_url="login")
def profile(request):
    return render(request, "profile.html")


@staff_member_required(login_url="login")
def adminPage(request):
    return render(request, "admin.html")


@staff_member_required(login_url="login")
def addQuiz(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Quiz.objects.create(title=title, description=description)
        messages.success(request, "Quiz added successfully.")
        return redirect("admin")
    return render(request, "add_quiz.html")


@staff_member_required(login_url="login")
def adminDashboard(request):
    quizzes = Quiz.objects.all()
    paginator = Paginator(quizzes, 10)  # Show 10 quizzes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin_dashboard.html", {"page_obj": page_obj})


def contactus(request):
    return render(request, "contactus.html")


def aboutus(request):
    return render(request, "aboutus.html")


@staff_member_required(login_url="login")
def updateQuiz(request, pk):
    quiz = Quiz.objects.get(id=pk)
    if request.method == "POST":
        quiz.title = request.POST.get("title")
        quiz.description = request.POST.get("description")
        quiz.save()
        messages.success(request, "Quiz updated successfully.")
        return redirect("admin")
    return render(request, "update_quiz.html", {"quiz": quiz})


@staff_member_required(login_url="login")
def deleteQuiz(request, pk):
    quiz = Quiz.objects.get(id=pk)
    if request.method == "POST":
        quiz.delete()
        messages.success(request, "Quiz deleted successfully.")
        return redirect("admin")
    return render(request, "delete_quiz.html", {"quiz": quiz})


@staff_member_required(login_url="login")
def addQuestion(request):
    quizzes = Quiz.objects.all()
    if request.method == "POST":
        quiz_id = request.POST.get("quiz")
        text = request.POST.get("text")
        option1 = request.POST.get("option1")
        option2 = request.POST.get("option2")
        option3 = request.POST.get("option3")
        option4 = request.POST.get("option4")
        correct_option = request.POST.get("correct_option")
        quiz = Quiz.objects.get(id=quiz_id)
        Question.objects.create(
            quiz=quiz,
            text=text,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_option=correct_option,
        )
        messages.success(request, "Question added successfully.")
        return redirect("admin")
    return render(request, "add_question.html", {"quizzes": quizzes})


@login_required(login_url="login")
def userDashboard(request):
    results = Result.objects.filter(user=request.user).order_by('-date_taken')
    return render(request, "user_dashboard.html", {"results": results})

