# Generated by Django 4.2.1 on 2023-06-04 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='user',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(blank=True, default=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
    ]