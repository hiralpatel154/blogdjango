# Generated by Django 3.0.8 on 2020-08-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Tech Blog', max_length=255),
        ),
    ]
