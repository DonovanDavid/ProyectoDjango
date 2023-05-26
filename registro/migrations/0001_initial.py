# Generated by Django 4.2.1 on 2023-05-07 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='tipoDocumento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('documento', models.IntegerField(max_length=15)),
                ('fechaNacimiento', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(max_length=10)),
                ('usuario', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('lugarResidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.ciudad')),
                ('tipoDocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.tipodocumento')),
            ],
        ),
    ]
