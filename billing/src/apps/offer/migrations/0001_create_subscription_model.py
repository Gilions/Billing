# Generated by Django 4.0 on 2022-09-11 13:14

import uuid

from django.db import migrations, models


def added_default_subscribe(apps, schema_editor):
    data = []
    model = apps.get_model('offer', 'Subscription')
    bronze = dict(name='Bronze', description='Стартовая подписка.', price=169)
    silver = dict(name='Silver', description='Расширенная подписка.', price=250)
    gold = dict(name='Golden', description='Премиальная подписка', price=560)

    for sub in (bronze, silver, gold):
        data.append(model(**sub))
    model.objects.bulk_create(data)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, help_text='Максимальная длина - 255 символов.', max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, help_text='Описание подписки.', null=True, verbose_name='Описание')),
                ('type', models.CharField(choices=[('enable', 'Включена'), ('disable', 'Выключена'), ('archive', 'Архив')], default='enable', help_text='Необходимо выбрать из представленных.', max_length=25, verbose_name='Тип подписки')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Стоимость')),
                ('currency', models.CharField(choices=[('RUB', 'Рубль'), ('USD', 'Доллар'), ('EUR', 'Евро')], default='RUB', max_length=3, verbose_name='Валюта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания.')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления.')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
                'ordering': ['-created_at'],
            },
        ),
        migrations.RunPython(added_default_subscribe)
    ]
