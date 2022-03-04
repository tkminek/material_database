# Generated by Django 4.0.2 on 2022-03-04 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_hose_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FibreOrientation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plastic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('material_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.materialtype')),
            ],
        ),
        migrations.CreateModel(
            name='WaterContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('plastic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plastic')),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('water_content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.watercontent')),
            ],
        ),
        migrations.CreateModel(
            name='PlasticInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('E', models.FloatField()),
                ('nu', models.FloatField(blank=True)),
                ('Rm', models.FloatField(blank=True)),
                ('Re', models.FloatField(blank=True)),
                ('Ru', models.FloatField(blank=True)),
                ('comment', models.CharField(max_length=1000)),
                ('temperature_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fibreorientation')),
            ],
        ),
        migrations.AddField(
            model_name='fibreorientation',
            name='fibre_orientation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.temperature'),
        ),
    ]
