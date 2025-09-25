from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
import openai   # Make sure to install: pip install openai
import os

# Set API key (Best practice: keep in .env or settings.py)
openai.api_key = os.getenv("OPENAI_API_KEY")

def home(request):
    return render(request, "home.html")

def loginPage(request):
    return render(request, "login.html")

def logoutUser(request):
    return redirect("home")

def register(request):
    return render(request, "register.html")

def quiz(request, pk):
    return render(request, "quiz.html", {"quiz_id": pk})

def result(request):
    return render(request, "result.html")

def profile(request):
    return render(request, "profile.html")

def adminPage(request):
    return render(request, "admin.html")

def addQuiz(request):
    return render(request, "pdfupload.html")

def adminDashboard(request):
    return render(request, "admindashboard.html")
 
def contactus(request):
    return render(request, "contactus.html")

def aboutus(request):
    return render(request, "aboutus.html")

def updateQuiz(request, pk):
    return render(request, "update_quiz.html", {"quiz_id": pk})

def deleteQuiz(request, pk):
    return redirect("home")

def addQuestion(request):
    return render(request, "add_question.html")

def userDashboard(request):
    return render(request, "user_dashboard.html")


# AI Suggestion Engine
def aiSuggest(request):
    if request.method == "POST":
        user_input = request.POST.get("query", "")
        if not user_input.strip():
            return JsonResponse({"error": "No query provided."}, status=400)

        try:
            response = openai.Completion.create(
                model="text-davinci-003",  # or gpt-3.5-turbo
                prompt=f"Give me suggestions for: {user_input}",
                max_tokens=150,
                temperature=0.7,
            )
            suggestion = response["choices"][0]["text"].strip()
            return JsonResponse({"suggestion": suggestion})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "ai_suggest.html")  # HTML page with form

from django.shortcuts import render, redirect, get_object_or_404
from pdfupload.models import UploadedPDF

def admindashboard(request):
    if request.method == "POST":
        if "pdf_file" in request.FILES:  # Handle upload
            pdf = request.FILES["pdf_file"]
            UploadedPDF.objects.create(file=pdf)
            return redirect("admindashboard")

        elif "delete_id" in request.POST:  # Handle delete
            pdf_id = request.POST.get("delete_id")
            pdf_obj = get_object_or_404(UploadedPDF, id=pdf_id)
            pdf_obj.file.delete(save=False)  # delete from storage
            pdf_obj.delete()  # delete from DB
            return redirect("admindashboard")

    pdfs = UploadedPDF.objects.all().order_by("-uploaded_at")
    return render(request, "admindashboard.html", {"pdfs": pdfs})
