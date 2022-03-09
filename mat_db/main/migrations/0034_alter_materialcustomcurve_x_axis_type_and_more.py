# Generated by Django 4.0.2 on 2022-03-09 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_alter_materialcustomcurve_x_axis_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialcustomcurve',
            name='x_axis_type',
            field=models.CharField(choices=[(' lin ', ' lin '), (' log ', ' log ')], max_length=200),
        ),
        migrations.AlterField(
            model_name='materialcustomcurve',
            name='y_axis_type',
            field=models.CharField(choices=[(' lin ', ' lin '), (' log ', ' log ')], max_length=200),
        ),
    ]
