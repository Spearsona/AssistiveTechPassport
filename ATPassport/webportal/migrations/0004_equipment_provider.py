# Generated by Django 4.2 on 2023-04-22 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0003_equipment_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='provider',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='webportal.provider'),
            preserve_default=False,
        ),
    ]