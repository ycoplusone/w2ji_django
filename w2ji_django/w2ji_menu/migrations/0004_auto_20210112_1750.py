# Generated by Django 3.0.7 on 2021-01-12 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('w2ji_menu', '0003_auto_20210112_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='group_nm',
            new_name='group',
        ),
    ]