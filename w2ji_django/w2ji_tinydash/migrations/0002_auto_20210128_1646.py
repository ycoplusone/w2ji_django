# Generated by Django 3.0.7 on 2021-01-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w2ji_tinydash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='작성일'),
        ),
    ]
