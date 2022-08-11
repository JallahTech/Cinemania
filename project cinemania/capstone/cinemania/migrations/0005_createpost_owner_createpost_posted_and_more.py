# Generated by Django 4.0.6 on 2022-08-01 17:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cinemania', '0004_createpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='createpost',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cinemania.signup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createpost',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 1, 17, 14, 41, 792206, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='createpost',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='movie_actors',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='movie_poster',
            field=models.ImageField(default='icon.jpg', upload_to='movies'),
        ),
    ]