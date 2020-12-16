# Generated by Django 3.0.7 on 2020-12-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=126, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('auther', models.CharField(max_length=16, verbose_name='작성자')),
                ('create_dt', models.DateTimeField(verbose_name='작성일')),
                ('update_dt', models.DateTimeField(auto_now_add=True, verbose_name='수정일')),
            ],
            options={
                'db_table': 'w2ji_bbs',
            },
        ),
    ]