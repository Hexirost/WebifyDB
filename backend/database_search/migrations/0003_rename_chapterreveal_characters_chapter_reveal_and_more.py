# Generated by Django 4.2.6 on 2023-10-27 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database_search', '0002_alter_characters_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characters',
            old_name='ChapterReveal',
            new_name='chapter_reveal',
        ),
        migrations.RenameField(
            model_name='characters',
            old_name='EpisodeReveal',
            new_name='episode_reveal',
        ),
        migrations.RenameField(
            model_name='characters',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='characters',
            old_name='Notes',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='characters',
            old_name='YearReveal',
            new_name='year_reveal',
        ),
    ]
