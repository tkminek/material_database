# Generated by Django 4.0.2 on 2022-03-05 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_fibrestaticcurve_fibresncurve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fibreorientation',
            name='comment',
        ),
    ]
