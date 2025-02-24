# Generated by Django 5.1.6 on 2025-02-24 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('equipo_casa_nombre', models.CharField(max_length=30)),
                ('equipo_visitante_nombre', models.CharField(max_length=30)),
                ('goles_casa', models.IntegerField()),
                ('goles_visitante', models.IntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('equipo_casa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_casa', to='Login.equipo')),
                ('equipo_visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos_visitante', to='Login.equipo')),
            ],
        ),
    ]
