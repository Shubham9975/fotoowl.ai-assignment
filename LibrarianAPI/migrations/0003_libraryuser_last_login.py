# Generated by Django 5.1.4 on 2024-12-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibrarianAPI', '0002_alter_libraryuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryuser',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
