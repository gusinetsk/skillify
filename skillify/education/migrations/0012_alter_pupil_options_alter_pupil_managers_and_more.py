# Generated by Django 4.2.3 on 2023-08-07 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0011_alter_pupil_options_alter_pupil_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pupil',
            options={},
        ),
        migrations.AlterModelManagers(
            name='pupil',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='name',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='password',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='username',
        ),
        migrations.AddField(
            model_name='pupil',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]