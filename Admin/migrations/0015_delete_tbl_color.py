# Generated by Django 5.0.1 on 2024-02-23 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_tbl_subcategory'),
        ('Designer', '0003_delete_tbl_designerwork'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_color',
        ),
    ]
