# Generated by Django 4.0.2 on 2022-03-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_alter_materialcustomcurve_x_axis_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialcustomcurve',
            name='x_axis_type',
            field=models.CharField(choices=[('lin', 'lin'), ('log', 'log')], max_length=200),
        ),
    ]
