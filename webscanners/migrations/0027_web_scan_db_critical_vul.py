# Generated by Django 3.2.15 on 2022-08-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscanners', '0026_auto_20210719_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='web_scan_db',
            name='critical_vul',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
