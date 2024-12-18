from django.core.management.base import BaseCommand
from quiz.models import Question, Quizsession

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        questions = [
            {"text": "What is 2 + 2?", "choice_a": "3", "choice_b": "4", "choice_c": "5", "choice_d": "6", "correct_answer": "B"},
            {"text": "What is 5 x 6?", "choice_a": "30", "choice_b": "25", "choice_c": "36", "choice_d": "40", "correct_answer": "A"},
            {"text": "What is the capital of Germany?", "choice_a": "New Delhi", "choice_b": "Madrid", "choice_c": "Berlin", "choice_d": "Rome", "correct_answer": "C"},
        ]

        # Iterate over the list of questions
        for question_data in questions:
            Question.objects.create(
                text=question_data['text'],
                choice_a=question_data['choice_a'],
                choice_b=question_data['choice_b'],
                choice_c=question_data['choice_c'],
                choice_d=question_data['choice_d'],
                correct_answer=question_data['correct_answer']
            )

        Quizsession.objects.create(total_questions=3, correct_answers=2, incorrect_answers=1)