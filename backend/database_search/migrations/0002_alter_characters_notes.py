# Generated by Django 4.2.6 on 2023-10-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='Notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
