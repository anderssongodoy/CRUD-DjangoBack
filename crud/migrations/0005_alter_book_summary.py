# Generated by Django 5.0.6 on 2024-06-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_book_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]