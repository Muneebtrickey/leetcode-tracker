from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Problem, DailyProgress, Streak


# 🏠 Home Dashboard
@login_required
def home(request):
    problems = Problem.objects.filter(user=request.user).order_by('-date_solved')

    # 📊 Stats
    total = problems.count()
    easy = problems.filter(difficulty='Easy').count()
    medium = problems.filter(difficulty='Medium').count()
    hard = problems.filter(difficulty='Hard').count()

    # 🔥 Streak
    streak, created = Streak.objects.get_or_create(user=request.user)

    context = {
        'problems': problems,
        'total': total,
        'easy': easy,
        'medium': medium,
        'hard': hard,
        'streak': streak.current_streak,
    }

    return render(request, 'home.html', context)


# ➕ Add Problem
@login_required
def add_problem(request):
    if request.method == "POST":
        title = request.POST.get('title')
        difficulty = request.POST.get('difficulty')
        problem_url = request.POST.get('problem_url')
        time_taken = request.POST.get('time_taken')

        # Create Problem
        Problem.objects.create(
            user=request.user,
            title=title,
            difficulty=difficulty,
            problem_url=problem_url,
            time_taken=time_taken if time_taken else None,
        )

        # 📊 Daily Progress
        today = timezone.now().date()
        daily, _ = DailyProgress.objects.get_or_create(
            user=request.user,
            date=today
        )
        daily.problems_solved += 1
        daily.save()

        # 🔥 Streak Logic
        streak, _ = Streak.objects.get_or_create(user=request.user)

        if streak.last_solved_date:
            delta = (today - streak.last_solved_date).days

            if delta == 1:
                streak.current_streak += 1
            elif delta > 1:
                streak.current_streak = 1
        else:
            streak.current_streak = 1

        streak.last_solved_date = today

        if streak.current_streak > streak.longest_streak:
            streak.longest_streak = streak.current_streak

        streak.save()

        return redirect('home')

    return render(request, 'add.html')


# ⭐ Toggle Favorite
@login_required
def toggle_favorite(request, pk):
    problem = Problem.objects.get(id=pk, user=request.user)
    problem.is_favorite = not problem.is_favorite
    problem.save()
    return redirect('home')


# 🗑 Delete Problem
@login_required
def delete_problem(request, pk):
    problem = Problem.objects.get(id=pk, user=request.user)
    problem.delete()
    return redirect('home')