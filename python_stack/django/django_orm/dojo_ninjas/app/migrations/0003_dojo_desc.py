# Generated by Django 2.0 on 2019-10-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_ninja_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojo'),
            preserve_default=False,
        ),
    ]
