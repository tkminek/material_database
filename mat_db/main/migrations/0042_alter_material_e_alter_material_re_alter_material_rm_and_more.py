# Generated by Django 4.0.2 on 2022-03-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_rename_model_type_rubbercustomcurve_curve_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='E',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='material',
            name='Re',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='material',
            name='Rm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='material',
            name='Ru',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='material',
            name='nu',
            field=models.FloatField(),
        ),
    ]