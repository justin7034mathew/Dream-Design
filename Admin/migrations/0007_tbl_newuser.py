# Generated by Django 5.0.1 on 2024-02-12 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_newUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newUser_name', models.CharField(max_length=30)),
                ('newUser_contact', models.CharField(max_length=30)),
                ('newUser_email', models.CharField(max_length=30)),
                ('newUser_gender', models.CharField(max_length=30)),
                ('newUser_address', models.CharField(max_length=30)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_district')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
