from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils import timezone
from django.db.models import Count
from .models import Problem, DailyProgress, Streak
from .forms import RegistrationForm, ProblemForm

# 🏠 Home Dashboard
@login_required
def home(request):
    """
    Renders the main dashboard for the user, displaying stats,
    recent problems, and a visual overview of their progress.
    """
    problems = Problem.objects.filter(user=request.user).order_by('-date_solved')

    # 📊 Statistical Summaries
    total_count = problems.count()
    difficulty_stats = problems.values('difficulty').annotate(count=Count('id'))
    
    # Initialize counts for difficulty for charts and UI cards
    stats = {
        'Easy': 0,
        'Medium': 0,
        'Hard': 0,
        'total': total_count
    }
    for entry in difficulty_stats:
        stats[entry['difficulty']] = entry['count']

    # 🔥 Streak Analysis
    streak, created = Streak.objects.get_or_create(user=request.user)

    context = {
        'problems': problems[:10], # Only show last 10 problems on dashboard
        'stats': stats,
        'streak_count': streak.current_streak,
        'longest_streak': streak.longest_streak,
        # Data for Chart.js
        'chart_labels': ['Easy', 'Medium', 'Hard'],
        'chart_data': [stats['Easy'], stats['Medium'], stats['Hard']]
    }

    return render(request, 'home.html', context)


# ➕ Add Problem
@login_required
def add_problem(request):
    """
    Handles the addition of new LeetCode problems solved by the user.
    Includes logic to update daily progress and user streaks.
    """
    if request.method == "POST":
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()

            # 📊 Increment Daily Progress Tracking
            today = timezone.now().date()
            daily, _ = DailyProgress.objects.get_or_create(user=request.user, date=today)
            daily.problems_solved += 1
            daily.save()

            # 🔥 Streak Logic Management
            update_user_streak(request.user, today)

            return redirect('home')
    else:
        form = ProblemForm()

    return render(request, 'add.html', {'form': form, 'title': 'Add Problem'})


# 📝 Edit Problem
@login_required
def edit_problem(request, pk):
    """
    Allows users to modify details of an existing problem entry.
    """
    problem = get_object_or_404(Problem, id=pk, user=request.user)
    if request.method == "POST":
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProblemForm(instance=problem)
    
    return render(request, 'add.html', {'form': form, 'title': 'Edit Problem', 'editing': True})


# ⭐ Toggle Favorite
@login_required
def toggle_favorite(request, pk):
    """
    Toggles the 'favorite' status of a specific problem.
    """
    problem = get_object_or_404(Problem, id=pk, user=request.user)
    problem.is_favorite = not problem.is_favorite
    problem.save()
    return redirect('home')


# 🗑 Delete Problem
@login_required
def delete_problem(request, pk):
    """
    Deletes a specific problem record from the user's history.
    """
    problem = get_object_or_404(Problem, id=pk, user=request.user)
    problem.delete()
    return redirect('home')


# 👤 User Registration
def signup(request):
    """
    Handles new user registration, creating both the User object 
    and ensuring necessary profile-related models are initialized.
    """
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Auto-login the user after registration
            login(request, user)
            
            # Initialize streak for the new user
            Streak.objects.create(user=user)
            
            return redirect('home')
    else:
        form = RegistrationForm()
    
    return render(request, 'signup.html', {'form': form})


def update_user_streak(user, today):
    """
    Helper function to calculate and update a user's problem-solving streak.
    """
    streak, _ = Streak.objects.get_or_create(user=user)

    if streak.last_solved_date:
        delta = (today - streak.last_solved_date).days

        if delta == 1:
            streak.current_streak += 1
        elif delta > 1:
            streak.current_streak = 1
        # If delta is 0, they already solved something today, streak remains same
    else:
        # First time solving
        streak.current_streak = 1

    streak.last_solved_date = today

    if streak.current_streak > streak.longest_streak:
        streak.longest_streak = streak.current_streak

    streak.save()
