# Generated by Django 2.2.2 on 2019-06-25 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpaceVehicleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BillOfMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('space_vehicle_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.SpaceVehicleOrder')),
                ('work_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.WorkCenter')),
            ],
        ),
    ]
