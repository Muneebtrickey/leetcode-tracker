from django.shortcuts import render
from .models import Problem

def home(request):
    problems = Problem.objects.all().order_by('-date_solved')
    return render(request, 'home.html', {'problems': problems})