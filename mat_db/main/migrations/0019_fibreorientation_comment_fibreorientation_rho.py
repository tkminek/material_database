# Generated by Django 4.0.2 on 2022-03-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_fibreorientation_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='fibreorientation',
            name='comment',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='fibreorientation',
            name='rho',
            field=models.FloatField(blank=True, default=5),
        ),
    ]
