# Generated by Django 5.0.4 on 2024-04-24 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='apeido_Materno',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidato',
            name='apeido_Paterno',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidato',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagen'),
        ),
        migrations.AddField(
            model_name='partido',
            name='descripcion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='votacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.candidato')),
            ],
        ),
    ]