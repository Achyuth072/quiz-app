from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question, Quizsession
import random

def start_quiz(request):
    """Start a new quiz session."""
    session = Quizsession.objects.create(total_questions=0, correct_answers=0, incorrect_answers=0)
    return redirect('quiz:question', session_id=session.id)

def get_question(request, session_id):
    """Fetch a random unanswered question or redirect to the results page."""
    session = Quizsession.objects.get(id=session_id)
    unanswered_questions = Question.objects.exclude(id__in=session.answered_questions.all())

    if not unanswered_questions.exists():
        # If no unanswered questions, redirect to results
        return redirect('quiz:results', session_id=session.id)

    # Get a random unanswered question
    question = random.choice(unanswered_questions)
    return render(request, 'quiz/question.html', {'question': question, 'session': session})

def submit_answer(request, session_id):
    """Check the submitted answer and update the session."""
    if request.method == 'POST':
        session = Quizsession.objects.get(id=session_id)
        question_id = request.POST['question_id']
        selected_choice = request.POST['choice']

        question = Question.objects.get(id=question_id)
        session.total_questions += 1

        # Mark the question as answered
        session.answered_questions.add(question)

        if question.correct_answer == selected_choice:
            session.correct_answers += 1
        else:
            session.incorrect_answers += 1

        session.save()
        return redirect('quiz:question', session_id=session.id)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_results(request, session_id):
    """Display the results of the quiz session."""
    session = Quizsession.objects.get(id=session_id)
    return render(request, 'quiz/results.html', {'session': session})
