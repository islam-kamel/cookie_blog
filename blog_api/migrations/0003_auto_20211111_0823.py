# Generated by Django 3.2.9 on 2021-11-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0002_alter_posts_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='tags',
        ),
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(related_name='post_tags', to='blog_api.Tags'),
        ),
    ]
