# Generated by Django 4.0.2 on 2022-02-15 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cycliccurve',
            old_name='material',
            new_name='material_id',
        ),
        migrations.RenameField(
            model_name='encurve',
            old_name='material',
            new_name='material_id',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='material_type',
            new_name='material_type_id',
        ),
        migrations.RenameField(
            model_name='sncurve',
            old_name='material',
            new_name='material_id',
        ),
    ]