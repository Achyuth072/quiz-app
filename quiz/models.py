from django.db import models


class Question(models.Model):
    text: models.CharField  # Annotation to indicate this is a CharField
    choice_a: models.CharField
    choice_b: models.CharField
    choice_c: models.CharField
    choice_d: models.CharField
    correct_answer: models.CharField

    text = models.CharField(max_length=255, default="Default question text")
    choice_a = models.CharField(max_length=100)
    choice_b = models.CharField(max_length=100)
    choice_c = models.CharField(max_length=100)
    choice_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1)  # e.g., "A", "B", "C", "D"

    def __str__(self) -> str:
        return self.text


class Quizsession(models.Model):
    total_questions: models.PositiveIntegerField
    correct_answers: models.PositiveIntegerField
    incorrect_answers: models.PositiveIntegerField

    total_questions = models.PositiveIntegerField(default=0)
    correct_answers = models.PositiveIntegerField(default=0)
    incorrect_answers = models.PositiveIntegerField(default=0)
    answered_questions = models.ManyToManyField(Question, blank=True)

    def __str__(self) -> str:
        return f"Session: {self.pk}"
