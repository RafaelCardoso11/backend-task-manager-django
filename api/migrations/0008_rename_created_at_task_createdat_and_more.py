# Generated by Django 4.2.6 on 2023-10-07 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_task_duedate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='updated_at',
            new_name='updatedAt',
        ),
    ]