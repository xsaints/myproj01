# Generated by Django 4.0.6 on 2022-08-10 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('justwork', '0004_alter_employee_manager_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='manager_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='justwork.employee'),
        ),
    ]
