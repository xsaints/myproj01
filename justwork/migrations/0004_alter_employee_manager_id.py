# Generated by Django 4.0.6 on 2022-08-10 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('justwork', '0003_alter_employee_department_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='manager_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='justwork.employee'),
        ),
    ]
