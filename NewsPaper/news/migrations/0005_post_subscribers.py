# Generated by Django 4.2.2 on 2023-07-17 10:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_alter_author_user_alter_comment_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
