# Generated by Django 4.0 on 2022-01-01 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieCllecReady',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('userId', models.IntegerField()),
                ('movieId', models.IntegerField()),
                ('is_collect', models.BooleanField()),
                ('is_towatch', models.BooleanField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieTop',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('movieId', models.IntegerField(primary_key=True, serialize=False)),
                ('avg_rating', models.FloatField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RatingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('userId', models.IntegerField()),
                ('movieId', models.IntegerField()),
                ('rating', models.FloatField()),
                ('content', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('userId', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('accont', models.IntegerField(unique=True)),
                ('nickname', models.TextField()),
                ('phone', models.IntegerField()),
                ('password', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
