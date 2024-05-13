# Generated by Django 5.0.1 on 2024-02-23 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0016_tbl_color'),
        ('Designer', '0003_delete_tbl_designerwork'),
        ('Guest', '0006_delete_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_designerwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_details', models.CharField(max_length=50)),
                ('designerwork_photo', models.FileField(upload_to='Assets/DesignerworkPhoto/')),
                ('designerwork_rate', models.IntegerField()),
                ('designerwork_duration', models.TimeField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_color')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_designer')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_material')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_subcategory')),
            ],
        ),
    ]
