# Generated by Django 5.1.4 on 2024-12-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_question_question_text_question_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsession',
            name='answered_questions',
            field=models.ManyToManyField(blank=True, to='quiz.question'),
        ),
    ]
