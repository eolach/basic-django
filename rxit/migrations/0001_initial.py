# Generated by Django 2.1.3 on 2018-11-07 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('province', models.CharField(default='', max_length=100)),
            ],
            options={
                'ordering': ('province',),
            },
        ),
    ]
