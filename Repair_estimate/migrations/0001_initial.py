# Generated by Django 3.1.7 on 2021-04-02 18:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Car_Base', '0004_auto_20210402_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repair_costs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_owner', models.CharField(max_length=50)),
                ('surname_owner', models.CharField(max_length=50)),
                ('date_of_accident', models.DateField(default=datetime.date(2021, 4, 2))),
                ('cost', models.FloatField(default=0.0)),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car_Base.carbrand')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car_Base.carmodel')),
                ('car_parts', models.ManyToManyField(to='Car_Base.CarParts')),
                ('parts_category', models.ManyToManyField(to='Car_Base.PartsCategory')),
            ],
        ),
    ]
