from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Custom User Model (Extending Django's default User)
class CustomUser(AbstractUser):
    # You can add extra fields here if needed
    # Example: bio, profile picture, etc.
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


# Quiz model
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Question model
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.text} (Quiz: {self.quiz.title})"


# Result model
class Result(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - Score: {self.score}"
