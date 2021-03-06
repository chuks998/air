# Generated by Django 3.1.5 on 2021-06-22 15:14

from django.db import migrations, models
import django.utils.timezone
import tracking_details.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Package_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracker', models.CharField(blank=True, default=tracking_details.models.id_genarator, max_length=7, null=True, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(default='None Added', max_length=50)),
                ('content', models.CharField(default='i-Phone12, D&G Designers Hand Bag', max_length=100)),
                ('date_pushed', models.DateField(default=django.utils.timezone.now)),
                ('delivery_date', models.DateField(default=tracking_details.models.limit_day)),
                ('progress', models.IntegerField(blank=True, default=tracking_details.models.next_day, null=True)),
                ('current_location', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='User_Package_Details',
        ),
    ]
