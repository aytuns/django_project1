# Generated by Django 4.2.1 on 2023-09-23 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_author_about_alter_author_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.TextField(default='I AM AN AUTHOR', max_length=500),
        ),
    ]