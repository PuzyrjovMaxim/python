# Generated by Django 5.0.6 on 2024-05-27 05:16

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular planet', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the name of the planet', max_length=200)),
                ('age', models.CharField(help_text='Enter the age of the planet', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular satellite', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the name of the satellite', max_length=200)),
                ('age', models.CharField(help_text='Enter the age of the satellite', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='order',
        ),
        migrations.CreateModel(
            name='Galaxy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular car', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the name of the car', max_length=200)),
                ('age', models.CharField(help_text='Enter the brand of the car', max_length=200)),
                ('planet', models.ForeignKey(help_text='Enter the id of the planet', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.planet')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='planet',
            name='satellite',
            field=models.ForeignKey(help_text='Enter the id of the satellite', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.satellite'),
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]