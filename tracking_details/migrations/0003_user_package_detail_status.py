# Generated by Django 3.1.5 on 2021-06-24 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_details', '0002_auto_20210622_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_package_detail',
            name='status',
            field=models.CharField(default={('delayed', 'delayed'), ('waiting comfirmation', 'waiting comfirmation'), ('pending', 'pending'), ('active', 'active')}, max_length=21),
        ),
    ]
