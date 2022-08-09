# Generated by Django 4.0.6 on 2022-08-08 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.IntegerField()),
                ('department_name', models.CharField(max_length=30)),
                ('manager_id', models.IntegerField()),
                ('location_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=20)),
                ('hire_date', models.DateField()),
                ('job_id', models.CharField(max_length=10)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commission_pct', models.DecimalField(decimal_places=2, max_digits=4)),
                ('manager_id', models.IntegerField()),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='justwork.department')),
            ],
        ),
    ]