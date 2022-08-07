# Generated by Django 4.0.6 on 2022-08-07 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txn_desc', models.CharField(max_length=80)),
                ('txn_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('txn_date', models.DateField()),
            ],
        ),
    ]