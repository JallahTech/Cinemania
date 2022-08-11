# Generated by Django 4.0.6 on 2022-08-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemania', '0005_createpost_owner_createpost_posted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=1000)),
                ('added', models.DateTimeField()),
            ],
        ),
    ]