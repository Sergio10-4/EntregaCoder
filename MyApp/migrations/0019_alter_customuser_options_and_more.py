# Generated by Django 4.2.2 on 2023-10-11 00:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0018_customuser_listadepeliculas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('username',), 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='descripcionUsuario',
            field=models.TextField(null=True, validators=[django.core.validators.MaxLengthValidator(250)]),
        ),
        migrations.AddField(
            model_name='customuser',
            name='fotoPerfil',
            field=models.ImageField(null=True, upload_to='perfilImages/'),
        ),
    ]
