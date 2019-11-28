# Generated by Django 2.2.7 on 2019-11-28 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0002_auto_20191127_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_items',
            fields=[
                ('item_id', models.CharField(max_length=1024, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=1024)),
                ('price', models.CharField(max_length=1024)),
                ('img_url', models.CharField(max_length=1024)),
                ('item_name', models.CharField(max_length=1024)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticator.User')),
            ],
        ),
    ]
