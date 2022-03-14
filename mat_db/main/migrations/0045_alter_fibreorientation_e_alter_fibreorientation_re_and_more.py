# Generated by Django 4.0.2 on 2022-03-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_hosedynamic_dyn_e_min40_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibreorientation',
            name='E',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fibreorientation',
            name='Re',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fibreorientation',
            name='Rm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fibreorientation',
            name='Ru',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fibreorientation',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='fibreorientation',
            name='nu',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fibreorientation',
            name='rho',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fibresncurve',
            name='Nf',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='fibresncurve',
            name='Sa',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='fibrestaticcurve',
            name='K',
            field=models.FloatField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fibrestaticcurve',
            name='n',
            field=models.FloatField(max_length=200),
        ),
        migrations.AlterField(
            model_name='rubbertemp',
            name='E',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rubbertemp',
            name='Re',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rubbertemp',
            name='Rm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rubbertemp',
            name='Ru',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rubbertemp',
            name='nu',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rubbertemp',
            name='rho',
            field=models.FloatField(),
        ),
    ]