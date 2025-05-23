# Generated by Django 5.1.1 on 2025-04-18 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('web_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('prefer_not_to_say', 'Prefer not to say'), ('others', 'Others')], max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('birthdate', models.DateField()),
                ('bio', models.TextField(blank=True, null=True)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='thriftapp.role')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('listing_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('condition', models.CharField(choices=[('brand_new', 'Brand New'), ('almost_new', 'Almost New'), ('slight_worn_off', 'Slightly Worn off'), ('quite_worn_off', 'Quite Worn off')], max_length=20)),
                ('status', models.CharField(choices=[('available', 'Available'), ('sold', 'Sold')], default='available', max_length=20)),
                ('listing_time', models.DateTimeField(auto_now_add=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thriftapp.webuser')),
            ],
        ),
    ]
