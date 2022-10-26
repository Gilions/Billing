# Generated by Django 4.0 on 2022-08-29 19:21

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationlog',
            name='stages_data',
            field=models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
    ]
