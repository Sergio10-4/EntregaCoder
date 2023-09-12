# Generated by Django 4.2.2 on 2023-09-12 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_serie_productoracinematografica'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pelicula',
            options={'ordering': ('nombre',), 'verbose_name': 'Pelicula', 'verbose_name_plural': 'Catalogo De Peliculas'},
        ),
        migrations.AlterModelOptions(
            name='productora',
            options={'ordering': ('nombre',), 'verbose_name': 'Productora', 'verbose_name_plural': 'Productoras De Cine'},
        ),
        migrations.AlterModelOptions(
            name='serie',
            options={'ordering': ('nombre',), 'verbose_name': 'Serie', 'verbose_name_plural': 'Catalogo De Series'},
        ),
    ]
