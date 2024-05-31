# Generated by Django 5.0.3 on 2024-04-02 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_profiles', to=settings.AUTH_USER_MODEL)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.experience')),
            ],
        ),
        migrations.CreateModel(
            name='HRProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pay', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('experience_required', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.experience')),
                ('hr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_skills', to='base.jobpost')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.skill')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to=settings.AUTH_USER_MODEL)),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='base.jobpost')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.status')),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_skills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
