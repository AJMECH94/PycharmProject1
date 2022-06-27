# Generated by Django 4.0.5 on 2022-06-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=1000)),
                ('Genres', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Mycollection',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=1000)),
                ('Genres', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Phone',
            field=models.CharField(max_length=10),
        ),
    ]