# Generated by Django 3.0.8 on 2020-07-02 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Compartimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
