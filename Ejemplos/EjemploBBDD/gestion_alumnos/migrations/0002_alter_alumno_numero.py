# Generated by Django 4.1.3 on 2023-02-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='numero',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
