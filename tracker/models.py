from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

"""
LeetCode Tracker Models
-----------------------
This file defines the data structure for the LC Tracker application.
It includes user profiles, problem entries, daily progress tracking, 
and user streaks.
"""

# 👤 User Profile
class UserProfile(models.Model):
    """
    Extends the default Django User model with LeetCode-specific details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leetcode_username = models.CharField(max_length=100, unique=True, help_text="Your public LeetCode handle")

    def __str__(self):
        return f"{self.user.username}'s Profile"


# 🏷️ Tag Model
class Tag(models.Model):
    """
    Categorization tags for problems (e.g., Dynamic Programming, Graph).
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# 📘 Problem Model
class Problem(models.Model):
    """
    The core model representing a solved or attempted LeetCode problem.
    Tracks difficulty, status, notes, and metadata for career portfolio display.
    """
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

    # Content
    title = models.CharField(max_length=255, help_text="The exact title of the problem")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Solved')

    # Metadata
    platform = models.CharField(max_length=100, default="LeetCode", help_text="Platform where the problem was solved")
    problem_url = models.URLField(blank=True, null=True, help_text="Direct link to the problem statement")

    # Relationships
    tags = models.ManyToManyField(Tag, blank=True, help_text="Select relevant algorithm/DS categories")

    # Performance
    time_taken = models.PositiveIntegerField(blank=True, null=True, help_text="Total minutes taken to solve")
    attempts = models.PositiveIntegerField(default=1, help_text="Number of attempts before success")

    # Journaling
    notes = models.TextField(blank=True, help_text="Document your approach or tricky edge cases")

    # Timestamps
    date_solved = models.DateField(default=timezone.now, help_text="The date this problem was completed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # UI Flags
    is_favorite = models.BooleanField(default=False, help_text="Mark for quick access or later review")

    class Meta:
        unique_together = ['user', 'title']
        ordering = ['-date_solved', '-created_at']
        verbose_name_plural = "Problems"

    def __str__(self):
        return f"{self.title} | {self.difficulty}"


# 📊 Daily Progress
class DailyProgress(models.Model):
    """
    Aggregated daily data for visualization in activity charts.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_progress')
    date = models.DateField(default=timezone.now)
    problems_solved = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ['user', 'date']
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} solved {self.problems_solved} on {self.date}"


# 🔥 Streak Model
class Streak(models.Model):
    """
    Maintains user motivation by tracking consecutive days of problem-solving.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    last_solved_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} | {self.current_streak} Day Streak"
