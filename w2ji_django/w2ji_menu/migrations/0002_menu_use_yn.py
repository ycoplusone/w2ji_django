# Generated by Django 3.0.7 on 2021-01-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w2ji_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='use_yn',
            field=models.BooleanField(null=True, verbose_name='사용여부'),
        ),
    ]
