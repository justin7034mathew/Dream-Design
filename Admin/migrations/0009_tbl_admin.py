# Generated by Django 5.0.1 on 2024-02-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_delete_tbl_newuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=30)),
            ],
        ),
    ]