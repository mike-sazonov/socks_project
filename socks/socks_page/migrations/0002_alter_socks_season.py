# Generated by Django 4.2.4 on 2024-02-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socks_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socks',
            name='season',
            field=models.CharField(choices=[('Зима', 'Зима'), ('Лето', 'Лето')], default='Лето', max_length=4),
        ),
    ]
