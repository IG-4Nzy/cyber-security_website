# Generated by Django 4.2.1 on 2023-06-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_problem_alter_register_email_alter_register_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_faced', models.CharField(max_length=100)),
                ('device_caused', models.CharField(max_length=100)),
                ('screenshot', models.ImageField(blank=True, upload_to='screenshots/')),
                ('other_details', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='problem',
        ),
    ]
