# Generated by Django 4.2.3 on 2023-07-31 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_pupil_photo_teacher_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='subject',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='education.subject', verbose_name='Предмет'),
        ),
        migrations.AddField(
            model_name='topic',
            name='grade_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.gradeclass', verbose_name='Класс'),
        ),
    ]
