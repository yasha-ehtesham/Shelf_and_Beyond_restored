# Generated by Django 5.2 on 2025-05-11 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thriftapp', '0018_alter_petadoption_age_alter_petadoption_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(choices=[('admin', 'Admin'), ('normal_user', 'Normal User')], max_length=20),
        ),
        migrations.CreateModel(
            name='AdoptionGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thriftapp.webuser')),
            ],
        ),
        migrations.AddField(
            model_name='adoptionapplication',
            name='adoption_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='thriftapp.adoptiongroup'),
        ),
    ]
