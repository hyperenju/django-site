# Generated by Django 3.1.5 on 2021-01-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processer', '0004_auto_20210122_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='firstFrameURL',
            field=models.CharField(default='', max_length=200),
        ),
    ]
