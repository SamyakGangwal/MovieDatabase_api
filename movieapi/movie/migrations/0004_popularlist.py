# Generated by Django 2.2.5 on 2019-11-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20191108_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('popularity', models.FloatField()),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
            ],
        ),
    ]
