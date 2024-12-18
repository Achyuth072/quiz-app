# Generated by Django 5.1.4 on 2024-12-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('choice_a', models.CharField(max_length=200)),
                ('choice_b', models.CharField(max_length=200)),
                ('choice_c', models.CharField(max_length=200)),
                ('choice_d', models.CharField(max_length=200)),
                ('correct_answer', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Quizsession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_questions', models.PositiveBigIntegerField(default=0)),
                ('correct_answers', models.PositiveBigIntegerField(default=0)),
                ('incorrect_answers', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]
