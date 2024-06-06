from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='login')
def home(request):
    questions = QuizQuestion.objects.all()
    return render(request, 'main/home.html',  {'questions': questions})

@login_required(login_url='login')
def about(request):
    return render(request, 'main/about.html')

def news(request):
    return render(request,'main/news.html')

def rules(request):
    return render(request,'main/rules.html')

def index(request):
    return render(request,'main/index.html')
    


def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass1') 
        user=authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('invalid user and password')
    return render(request, 'register/login.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass2!=pass1:
            return HttpResponse("Passwords don't match!")
        if pass2 == pass1:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            # return HttpResponse('User has been created')
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, "Passwords don't match.")
            # return HttpResponse("Passwords don't match.")
            return render(request , 'register/signup.html')
    return render(request, 'register/signup.html')

def logout(request):
    logout(request)
    return redirect('login')

def python(request):
    return render(request,'category/python/py.html')
def py1(request):
    questions=QuizQuestion.objects.filter(level='pbeginner')
    # print(questions)
    return render(request,'category/python/py1.html',{'questions':questions})
def py2(request):
    questions=QuizQuestion.objects.filter(level='pmedium')
    return render(request,'category/python/py2.html',{'questions':questions})
def py3(request):
    questions=QuizQuestion.objects.filter(level='phard')
    return render(request,'category/python/py3.html',{'questions':questions})

def result(request):
    if request.method == "POST":
        level=request.POST.get('level')
        user_answer, user_choice = [], []
        for i in range(1, 6):
            que_name = 'q' + str(i)
            que_choice = 'que' + str(i)
            user_answer.append(request.POST.get(que_name))
            user_choice.append(request.POST.get(que_choice))

        marks = []
        count = 0
        all_questions = QuizQuestion.objects.filter(level=level)
        for user_ans in user_answer:
            questions = QuizQuestion.objects.filter(id=user_ans).first()

            if questions.right_option == user_choice[count]:
                questions.points = 2
                marks.append(2)
            else:
                questions.points = 0
            count += 1
            questions.save()

 
        total_marks = sum(marks)

        quiz_result = QuizResult(
            user=request.user,
            level=level,
            total_marks=total_marks
        )
        quiz_result.save()


        question_choices = zip(all_questions, user_choice)
        return render(request, 'main/result.html', {'question_choices': question_choices, 'total_marks': total_marks})

        


def django(request):
    return render(request,'category/django/dj.html')
def dj1(request):
    questions=QuizQuestion.objects.filter(level='dbeginner')
    return render(request,'category/django/dj1.html',{'questions':questions})
def dj2(request):
    questions=QuizQuestion.objects.filter(level='dmedium')
    return render(request,'category/django/dj2.html',{'questions':questions})
def dj3(request):
    questions=QuizQuestion.objects.filter(level='dhard')
    return render(request,'category/django/dj3.html',{'questions':questions})


def cpp(request):
    return render(request,'category/CPP/cpp.html')
def cpp1(request):
    questions=QuizQuestion.objects.filter(level='cppbeginner')
    return render(request,'category/CPP/cpp1.html',{'questions':questions})
def cpp2(request):
    questions=QuizQuestion.objects.filter(level='cppmedium')
    return render(request,'category/CPP/cpp2.html',{'questions':questions})
def cpp3(request):
    questions=QuizQuestion.objects.filter(level='cpphard')
    return render(request,'category/CPP/cpp3.html',{'questions':questions})


def question_list(request):
    questions=Question.objects.filter(level='begn')
    print(questions)
    return render(request,'/category/python/py1.html', {'questions':questions})

