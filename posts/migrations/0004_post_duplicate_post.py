# Generated by Django 4.1.1 on 2023-02-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='duplicate_post',
            field=models.IntegerField(default=0),
        ),
    ]