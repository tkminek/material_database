# Generated by Django 4.0.2 on 2022-03-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_rubber_rubbertemp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubbertemp',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
