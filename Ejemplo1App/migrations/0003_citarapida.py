# Generated by Django 3.2.3 on 2021-06-05 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ejemplo1App', '0002_producto_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitaRapida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('cabello', models.TextField()),
                ('fecha', models.DateField()),
                ('hora', models.DateField()),
            ],
        ),
    ]
