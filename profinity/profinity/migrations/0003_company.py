# Generated by Django 5.0 on 2023-12-17 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profinity', '0002_rename_milestones_milestone_delete_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, upload_to='company_logo/')),
                ('number_of_employees', models.IntegerField()),
                ('Employees', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='profinity.employee')),
                ('departments', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='profinity.department')),
                ('projects', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='profinity.project')),
            ],
        ),
    ]
