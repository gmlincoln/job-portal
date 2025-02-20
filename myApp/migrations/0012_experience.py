# Generated by Django 5.1.1 on 2024-10-07 16:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_alter_degreetype_model_degree_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, null=True)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(max_length=100, null=True)),
                ('end_date', models.DateField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
