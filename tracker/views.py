from django.shortcuts import render, redirect
from .models import Problem

def home(request):
    problems = Problem.objects.all().order_by('-date_solved')
    return render(request, 'home.html', {'problems': problems})


def add_problem(request):
    if request.method == "POST":
        title = request.POST.get('title')
        difficulty = request.POST.get('difficulty')

        Problem.objects.create(
            title=title,
            difficulty=difficulty
        )

        return redirect('home')

    return render(request, 'add.html')