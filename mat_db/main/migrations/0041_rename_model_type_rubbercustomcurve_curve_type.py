# Generated by Django 4.0.2 on 2022-03-09 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_rename_curve_type_rubbercustomcurve_model_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rubbercustomcurve',
            old_name='model_type',
            new_name='curve_type',
        ),
    ]