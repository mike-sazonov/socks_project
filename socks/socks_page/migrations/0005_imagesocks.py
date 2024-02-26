# Generated by Django 4.2.4 on 2024-02-22 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socks_page', '0004_alter_socks_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='socks_gallery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socks_page.socks')),
            ],
        ),
    ]