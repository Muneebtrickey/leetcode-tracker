from django.urls import path
from . import views

urlpatterns = [
    # 🏠 Dashboard
    path('', views.home, name='home'),

    # ➕ Add Problem
    path('add/', views.add_problem, name='add_problem'),

    # ⭐ Mark as Favorite
    path('favorite/<int:pk>/', views.toggle_favorite, name='toggle_favorite'),

    # 🗑 Delete Problem
    path('delete/<int:pk>/', views.delete_problem, name='delete_problem'),
]