# Generated by Django 4.2 on 2023-04-22 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_bloguser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]