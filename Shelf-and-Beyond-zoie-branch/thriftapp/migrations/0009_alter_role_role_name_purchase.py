# Generated by Django 5.1.1 on 2025-05-04 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thriftapp', '0008_listing_author_alter_role_role_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(choices=[('normal_user', 'Normal User'), ('admin', 'Admin')], max_length=20),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('CONFIRMED', 'Confirmed'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], default='CONFIRMED', max_length=10)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='thriftapp.webuser')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thriftapp.listing')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='thriftapp.webuser')),
            ],
        ),
    ]
