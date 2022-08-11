# Generated by Django 4.0.6 on 2022-07-30 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemania', '0003_alter_signup_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('movie_date', models.DateField()),
                ('movie_actors', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('movie_genre', models.CharField(choices=[('Romantic', 'R'), ('Comedy', 'C'), ('Cartoon', 'K'), ('Actions', 'R')], max_length=15)),
                ('movie_poster', models.ImageField(upload_to='')),
            ],
        ),
    ]