# Generated by Django 4.2.3 on 2024-04-08 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommentApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
