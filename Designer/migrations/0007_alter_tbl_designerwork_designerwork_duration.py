# Generated by Django 5.0.1 on 2024-02-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Designer', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_designerwork',
            name='designerwork_duration',
            field=models.IntegerField(),
        ),
    ]