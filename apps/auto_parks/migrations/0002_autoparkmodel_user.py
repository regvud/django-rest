# Generated by Django 4.2.6 on 2023-10-10 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('auto_parks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoparkmodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='auto_parks', to='Users.usersmodel'),
            preserve_default=False,
        ),
    ]