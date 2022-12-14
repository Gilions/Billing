# Generated by Django 4.0 on 2022-09-11 12:01
import os

from django.db import migrations


def generate_superuser(apps, schema_editor):
    """Create a new superuser """
    # TODO: К финальному релизу нужно будет убрать эту миграцию
    from django.contrib.auth import get_user_model

    superuser = get_user_model().objects.create_superuser(
        username=os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin'),
        email=os.environ.get('DJANGO_SUPERUSER_EMAIL', 'test@admin.ru'),
        password=os.environ.get('DJANGO_SUPERUSER_PASSWORD', '123'),
    )
    superuser.save()


class Migration(migrations.Migration):
    dependencies = [('offer', '0001_create_subscription_model')
                    ]

    operations = [
        migrations.RunPython(generate_superuser),
    ]
