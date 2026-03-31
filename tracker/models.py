from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# 👤 User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leetcode_username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.user.username


# 🏷️ Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# 📘 Problem Model (ONLY ONE)
class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    STATUS_CHOICES = [
        ('Solved', 'Solved'),
        ('Attempted', 'Attempted'),
        ('Revision', 'Revision'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='problems')

    title = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Solved')

    platform = models.CharField(max_length=100, default="LeetCode")
    problem_url = models.URLField(blank=True, null=True)

    tags = models.ManyToManyField(Tag, blank=True)

    time_taken = models.PositiveIntegerField(blank=True, null=True)
    attempts = models.PositiveIntegerField(default=1)

    notes = models.TextField(blank=True)

    date_solved = models.DateField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_favorite = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'title']
        ordering = ['-date_solved']

    def __str__(self):
        return f"{self.title} ({self.difficulty})"


# 📊 Daily Progress
class DailyProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_progress')
    date = models.DateField(default=timezone.now)
    problems_solved = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ['user', 'date']
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date}"


# 🔥 Streak Model
class Streak(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    last_solved_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Streak: {self.current_streak}"