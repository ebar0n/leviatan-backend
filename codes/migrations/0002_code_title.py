# Generated by Django 2.1.7 on 2019-03-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
