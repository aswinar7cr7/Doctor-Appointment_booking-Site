# Generated by Django 5.1.2 on 2024-11-09 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yogaapp', '0005_alter_customer_time_alter_customer_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set(),
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
    ]