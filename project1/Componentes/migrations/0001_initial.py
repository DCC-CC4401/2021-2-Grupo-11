# Generated by Django 3.1.1 on 2021-09-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('frecuencia', models.CharField(max_length=20)),
                ('frecuencia_turbo', models.CharField(max_length=20)),
                ('cache', models.CharField(max_length=50)),
                ('socket', models.CharField(max_length=20)),
                ('nucleo', models.CharField(max_length=100)),
                ('proceso', models.CharField(max_length=20)),
                ('tdp', models.CharField(max_length=20)),
                ('cooler', models.CharField(max_length=50)),
                ('graficos', models.CharField(max_length=50)),
            ],
        ),
    ]