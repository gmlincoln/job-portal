# Generated by Django 5.1.1 on 2024-09-28 01:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_resume_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeType_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('degree_level', models.CharField(choices=[('ssc', 'SSC'), ('hsc', 'HSC'), ('diploma', 'Diploma'), ('bachelor', "Bachelor's Degree"), ('master', "Master's Degree"), ('phd', 'Doctorate (PhD)')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
