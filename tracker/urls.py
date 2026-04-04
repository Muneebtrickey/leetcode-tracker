from django.urls import path
from . import views

urlpatterns = [
    # 🏠 Dashboard
    path('', views.home, name='home'),

    # 👤 Authentication
    path('signup/', views.signup, name='signup'),

    # ➕ Problem Management
    path('add/', views.add_problem, name='add_problem'),
    path('edit/<int:pk>/', views.edit_problem, name='edit_problem'),

    # ⭐ Interactions
    path('favorite/<int:pk>/', views.toggle_favorite, name='toggle_favorite'),
    path('delete/<int:pk>/', views.delete_problem, name='delete_problem'),
]
