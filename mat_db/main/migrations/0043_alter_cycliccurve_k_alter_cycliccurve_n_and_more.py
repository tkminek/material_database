# Generated by Django 4.0.2 on 2022-03-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_alter_material_e_alter_material_re_alter_material_rm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cycliccurve',
            name='K',
            field=models.FloatField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cycliccurve',
            name='n',
            field=models.FloatField(max_length=200),
        ),
        migrations.AlterField(
            model_name='encurve',
            name='Ef',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='encurve',
            name='Sf',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='encurve',
            name='b',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='encurve',
            name='c',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sncurve',
            name='Nf',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='sncurve',
            name='Sa',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='staticcurve',
            name='K',
            field=models.FloatField(max_length=200),
        ),
        migrations.AlterField(
            model_name='staticcurve',
            name='n',
            field=models.FloatField(max_length=200),
        ),
    ]
