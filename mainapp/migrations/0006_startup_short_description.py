# Generated by Django 3.2.7 on 2021-09-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_startup_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='short_description',
            field=models.TextField(null=True, verbose_name='Короткий опис'),
        ),
    ]
