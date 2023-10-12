# Generated by Django 4.2.6 on 2023-10-12 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0002_autoparkmodel_user'),
        ('cars', '0007_alter_carmodel_auto_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='auto_park',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_parks.autoparkmodel'),
        ),
    ]