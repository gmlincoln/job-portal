# Generated by Django 5.1.1 on 2024-10-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_alter_degreetype_model_degree_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degreetype_model',
            name='degree_level',
            field=models.CharField(choices=[('ssc', 'SSC'), ('hsc', 'HSC'), ('diploma', 'Diploma'), ('bachelor', "Bachelor's Degree"), ('master', "Master's Degree"), ('phd', 'Doctorate (PhD)')], max_length=100, null=True),
        ),
    ]
