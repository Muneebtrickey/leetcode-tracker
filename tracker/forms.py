from django import forms
from django.contrib.auth.models import User
from .models import Problem

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'difficulty', 'status', 'platform', 'problem_url', 'time_taken', 'attempts', 'notes', 'is_favorite']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Two Sum'}),
            'difficulty': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'platform': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., LeetCode'}),
            'problem_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://leetcode.com/problems/...'}),
            'time_taken': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minutes taken'}),
            'attempts': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Key takeaways or approach...'}),
            'is_favorite': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
