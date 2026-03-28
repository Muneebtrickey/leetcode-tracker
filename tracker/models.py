from django.db import models

class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    platform = models.CharField(max_length=100, default="LeetCode")
    date_solved = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title