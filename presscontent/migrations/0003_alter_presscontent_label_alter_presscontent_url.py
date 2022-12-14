# Generated by Django 4.1.3 on 2022-11-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presscontent', '0002_alter_presscontent_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presscontent',
            name='label',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='presscontent',
            name='url',
            field=models.SlugField(editable=False, max_length=255, unique=True),
        ),
    ]
