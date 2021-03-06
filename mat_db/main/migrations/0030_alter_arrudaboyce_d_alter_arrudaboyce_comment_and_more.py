# Generated by Django 4.0.2 on 2022-03-09 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_neohooke'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrudaboyce',
            name='D',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='arrudaboyce',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='arrudaboyce',
            name='lambda_m',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='arrudaboyce',
            name='nu',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='cycliccurve',
            name='K',
            field=models.FloatField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='cycliccurve',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='cycliccurve',
            name='n',
            field=models.FloatField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='encurve',
            name='Ef',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='encurve',
            name='Sf',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='encurve',
            name='b',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='encurve',
            name='c',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='encurve',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='fibreorientation',
            name='E',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='fibresncurve',
            name='Nf',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='fibresncurve',
            name='Sa',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='fibresncurve',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='fibrestaticcurve',
            name='K',
            field=models.FloatField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='fibrestaticcurve',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='fibrestaticcurve',
            name='n',
            field=models.FloatField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='hosedynamic',
            name='Dyn_E_min40',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='hosedynamic',
            name='Dyn_E_plus100',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='hosedynamic',
            name='Dyn_E_plus23',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='hosedynamic',
            name='Dyn_comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='hosedynamic',
            name='Dyn_nu_min40',
            field=models.FloatField(blank=True, default=0.495),
        ),
        migrations.AlterField(
            model_name='hosedynamic',
            name='Dyn_nu_plus100',
            field=models.FloatField(blank=True, default=0.495),
        ),
        migrations.AlterField(
            model_name='hosedynamic',
            name='Dyn_nu_plus23',
            field=models.FloatField(blank=True, default=0.495),
        ),
        migrations.AlterField(
            model_name='hosestatic',
            name='Stat_E_min40',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='hosestatic',
            name='Stat_E_plus100',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='hosestatic',
            name='Stat_E_plus23',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='hosestatic',
            name='Stat_comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='hosestatic',
            name='Stat_nu_min40',
            field=models.FloatField(blank=True, default=0.495),
        ),
        migrations.AlterField(
            model_name='hosestatic',
            name='Stat_nu_plus100',
            field=models.FloatField(blank=True, default=0.495),
        ),
        migrations.AlterField(
            model_name='hosestatic',
            name='Stat_nu_plus23',
            field=models.FloatField(blank=True, default=0.495),
        ),
        migrations.AlterField(
            model_name='material',
            name='E',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='Re',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='Rm',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='Ru',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='material',
            name='nu',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='mooneyrivlin',
            name='C_01',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='mooneyrivlin',
            name='C_10',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='mooneyrivlin',
            name='D_1',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='mooneyrivlin',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='neohooke',
            name='C_10',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='neohooke',
            name='D_1',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='neohooke',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='ogden',
            name='D_1',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='ogden',
            name='alfa_1',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='ogden',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='ogden',
            name='nu_1',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='polynomial',
            name='C_10',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='polynomial',
            name='D_1',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='rubbertemp',
            name='E',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='rubbertemp',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='sncurve',
            name='Nf',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='sncurve',
            name='Sa',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='sncurve',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='staticcurve',
            name='K',
            field=models.FloatField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='staticcurve',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='staticcurve',
            name='n',
            field=models.FloatField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='yeoh',
            name='C_10',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='yeoh',
            name='C_20',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='yeoh',
            name='C_30',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='yeoh',
            name='D_1',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='yeoh',
            name='D_2',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='yeoh',
            name='D_3',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='yeoh',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.CreateModel(
            name='MaterialCustomCurve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('type', models.CharField(blank=True, max_length=20000)),
                ('x_axis', models.CharField(blank=True, max_length=20000)),
                ('x_value', models.CharField(blank=True, max_length=20000)),
                ('y_axis', models.CharField(blank=True, max_length=20000)),
                ('y_value', models.CharField(blank=True, max_length=20000)),
                ('comment', models.CharField(blank=True, max_length=1000)),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.material')),
            ],
        ),
    ]
