# Generated by Django 2.2.5 on 2020-08-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('star', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeptManager',
            fields=[
                ('dept_no', models.CharField(max_length=4)),
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
            options={
                'db_table': 'dept_manager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('salary', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
            options={
                'db_table': 'salaries',
                'managed': False,
            },
        ),
    ]