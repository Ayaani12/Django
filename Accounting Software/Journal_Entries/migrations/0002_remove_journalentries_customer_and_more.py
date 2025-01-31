# Generated by Django 5.0.7 on 2024-07-16 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Journal_Entries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalentries',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='journalentries',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='journalentries',
            name='project',
        ),
        migrations.RemoveField(
            model_name='journalentries',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='journalentrylines',
            name='journal_entry',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
        migrations.DeleteModel(
            name='JournalEntries',
        ),
        migrations.DeleteModel(
            name='JournalEntryLines',
        ),
    ]
