# Generated by Django 5.1.6 on 2025-02-24 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratiorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('numero_ordenadores', models.IntegerField()),
                ('email_tecnico', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Resolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_inc', models.IntegerField()),
                ('email_profesor', models.EmailField(max_length=254)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('numero_inc', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('numero_ordenador', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('email_profesor', models.EmailField(max_length=30)),
                ('resuelta', models.BooleanField(default=False)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gest_inc.laboratiorio')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=128)),
                ('laboratorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gest_inc.laboratiorio')),
            ],
        ),
    ]
