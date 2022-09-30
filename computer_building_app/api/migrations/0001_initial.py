# Generated by Django 4.1.1 on 2022-09-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Builds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(default='', max_length=8, unique=True)),
                ('budget', models.IntegerField(default=1000)),
                ('cpu_type', models.CharField(default='', max_length=5)),
                ('gpu_type', models.CharField(default='', max_length=7)),
                ('aio_pref', models.CharField(default='', max_length=1)),
                ('cpu_name', models.CharField(default='', max_length=50)),
                ('gpu_name', models.CharField(default='', max_length=50)),
                ('ram_name', models.CharField(default='', max_length=50)),
                ('mb_name', models.CharField(default='', max_length=50)),
                ('case_name', models.CharField(default='', max_length=50)),
                ('psu_name', models.CharField(default='', max_length=50)),
                ('ssd_name', models.CharField(default='', max_length=50)),
                ('aio_name', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
