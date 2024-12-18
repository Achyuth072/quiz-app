from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('start/', views.start_quiz, name='start'),
    path('<int:session_id>/question/', views.get_question, name='question'),
    path('<int:session_id>/submit/', views.submit_answer, name='submit'),
    path('<int:session_id>/results/', views.get_results, name='results'),
]
