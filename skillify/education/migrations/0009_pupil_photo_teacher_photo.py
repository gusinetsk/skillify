# Generated by Django 4.2.3 on 2023-07-31 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_alter_subject_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
    ]