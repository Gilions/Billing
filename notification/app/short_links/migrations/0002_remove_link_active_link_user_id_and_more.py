# Generated by Django 4.0 on 2022-09-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_links', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='active',
        ),
        migrations.AddField(
            model_name='link',
            name='user_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='link',
            name='redirect_url',
            field=models.URLField(default='https://movies_service_main_page'),
        ),
    ]