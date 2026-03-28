from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=10)
    platform = models.CharField(max_length=100, default="LeetCode")
    date_solved = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title