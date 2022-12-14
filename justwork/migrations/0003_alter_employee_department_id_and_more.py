# Generated by Django 4.0.6 on 2022-08-10 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('justwork', '0002_alter_department_department_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='justwork.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='manager_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='justwork.employee'),
        ),
    ]
