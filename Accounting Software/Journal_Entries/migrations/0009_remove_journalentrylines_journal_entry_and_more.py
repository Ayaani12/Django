# Generated by Django 5.0.7 on 2024-07-16 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Journal_Entries', '0008_alter_journalentrylines_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalentrylines',
            name='journal_entry',
        ),
        migrations.DeleteModel(
            name='JournalEntries',
        ),
        migrations.DeleteModel(
            name='JournalEntryLines',
        ),
    ]
