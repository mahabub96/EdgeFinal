# Generated by Django 5.1.4 on 2024-12-06 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auction_items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='auction_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('auction_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='auction_items.auctionitem')),
            ],
        ),
    ]
