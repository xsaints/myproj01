# Generated by Django 4.0.6 on 2022-08-10 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('justwork', '0006_remove_employee_commission_pct_remove_employee_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='location_id',
        ),
        migrations.AlterField(
            model_name='department',
            name='manager_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='justwork.employee'),
        ),
    ]
