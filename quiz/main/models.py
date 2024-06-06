from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuizCategory(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(default='not available')
    img = models.ImageField(upload_to="py1.jfif/",default="/static/img/py1.jfif/")


    def __str__(self):
        return self.name

class QuizQuestion(models.Model):
    category=models.ForeignKey(QuizCategory , on_delete=models.CASCADE)
    question_text=models.TextField()
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    level=models.CharField(max_length=100,default=0)
    points=models.IntegerField(default="0")
    time_limit=models.IntegerField()
    right_option=models.CharField(max_length=100)
    
    def __str__(self):
        return self.question_text

class QuizResult(models.Model):
    resultid = models.IntegerField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=10)
    right =models.IntegerField(default=0, null=True)
    wrong=models.IntegerField(default=0, null=True)
    total_marks = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.level} - {self.total_marks}"

class Question(models.Model):
    text=models.CharField(max_length=255)
    answer=models.CharField(max_length=255)
