# Generated by Django 4.1.7 on 2023-03-22 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birth_days',
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_days',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='birth'),
            preserve_default=False,
        ),
    ]
