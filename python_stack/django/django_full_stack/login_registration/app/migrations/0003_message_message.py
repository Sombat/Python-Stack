# Generated by Django 2.2.6 on 2019-10-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191017_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message',
            field=models.TextField(default='alfjas;llfjas'),
            preserve_default=False,
        ),
    ]