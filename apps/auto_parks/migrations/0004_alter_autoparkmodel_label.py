# Generated by Django 4.2.6 on 2023-10-13 10:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0003_alter_autoparkmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoparkmodel',
            name='label',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z\\D ]{1,20}$', 'First letter uppercase min 2 max 20 ch')]),
        ),
    ]
