# Generated by Django 5.1.3 on 2024-11-27 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0005_book_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='status',
            field=models.CharField(choices=[('DISPONIBLE', 'DISPONIBLE'), ('AGOTADO', 'AGOTADO')], default='DISPONIBLE', max_length=15),
        ),
    ]
