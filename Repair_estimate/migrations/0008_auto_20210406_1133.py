# Generated by Django 3.1.7 on 2021-04-06 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car_Base', '0004_auto_20210402_1124'),
        ('Repair_estimate', '0007_auto_20210406_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Car_Base.carparts'),
        ),
    ]
