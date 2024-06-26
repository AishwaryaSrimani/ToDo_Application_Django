# Generated by Django 5.0.4 on 2024-04-26 13:35

import todo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0006_task_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="username",
            field=models.CharField(
                default=todo.models.task.get_default_username, max_length=50
            ),
        ),
    ]
