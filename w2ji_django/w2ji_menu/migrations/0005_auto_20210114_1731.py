# Generated by Django 3.1 on 2021-01-14 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('w2ji_menu', '0004_auto_20210112_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='w2ji_menu.group'),
        ),
    ]