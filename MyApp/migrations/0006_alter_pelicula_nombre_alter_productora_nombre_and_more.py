# Generated by Django 4.2.2 on 2023-09-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_alter_pelicula_options_alter_productora_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productora',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='serie',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
